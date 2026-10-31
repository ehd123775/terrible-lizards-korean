"""Replace repository-owner commit emails, preserving every file tree."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import time

OWNER='ehd123775'
NOREPLY='350544894+ehd123775@users.noreply.github.com'
REPOSITORY='ehd123775/terrible-lizards-korean'

def git(repo, *args, data=None):
    return subprocess.check_output(['git','-C',str(repo),*args],input=data)

def rebuild(repo, refs):
    revisions=git(repo,'rev-list','--reverse','--topo-order',*dict.fromkeys(refs.values())).decode().splitlines()
    mapping={}; replaced=0
    for sha in revisions:
        raw=git(repo,'cat-file','commit',sha)
        header,message=raw.split(b'\n\n',1)
        blocks=[]
        for line in header.split(b'\n'):
            if line.startswith(b' '): blocks[-1]+=b'\n'+line
            else: blocks.append(line)
        clean=[]
        for block in blocks:
            if block.startswith((b'gpgsig ',b'mergetag ')): continue
            if block.startswith(b'parent '):
                block=b'parent '+mapping[block[7:].decode()].encode()
            match=re.fullmatch(rb'(author|committer) (.*) <([^<>]+)> ([0-9]+ [+-][0-9]{4})',block)
            if match:
                kind,name,email,stamp=match.groups()
                if email!=b'noreply@github.com' and not email.endswith(b'@users.noreply.github.com'):
                    assert name.decode()==OWNER, 'Unexpected author; no history changed'
                    block=kind+b' '+name+b' <'+NOREPLY.encode()+b'> '+stamp
                    replaced+=1
            clean.append(block)
        result=b'\n'.join(clean)+b'\n\n'+message
        new=git(repo,'hash-object','-t','commit','-w','--stdin',data=result).decode().strip()
        assert git(repo,'rev-parse',sha+'^{tree}')==git(repo,'rev-parse',new+'^{tree}')
        mapping[sha]=new
    for new in mapping.values():
        identities=git(repo,'show','-s','--format=%ae%n%ce',new).decode().splitlines()
        assert all(email=='noreply@github.com' or email.endswith('@users.noreply.github.com') for email in identities)
    return mapping,replaced

def api(method, endpoint, payload=None):
    args=['gh','api','--method',method,f'repos/{REPOSITORY}/{endpoint}']
    if payload is not None: args+=['--input','-']
    for attempt in range(5):
        p=subprocess.run(args,input=json.dumps(payload) if payload is not None else None,text=True,capture_output=True)
        if p.returncode==0:
            return json.loads(p.stdout) if p.stdout.strip() else None
        if method not in ['GET','PATCH','DELETE'] or attempt==4:
            raise RuntimeError('GitHub API request failed: '+p.stderr.strip())
        time.sleep(3)

def finish_clean_history(repo):
    clean=set(git(repo,'rev-list','HEAD').decode().splitlines())
    for sha in clean:
        emails=git(repo,'show','-s','--format=%ae%n%ce',sha).decode().splitlines()
        assert all(e=='noreply@github.com' or e.endswith('@users.noreply.github.com') for e in emails)
    for release in api('GET','releases'):
        target=git(repo,'rev-parse','refs/tags/'+release['tag_name']).decode().strip()
        assert target in clean
        digests={a['name']:a.get('digest') for a in release['assets']}
        if release['target_commitish']!=target:
            api('PATCH',f"releases/{release['id']}",{'target_commitish':target})
        after=api('GET',f"releases/{release['id']}")
        assert after['target_commitish']==target
        assert digests=={a['name']:a.get('digest') for a in after['assets']}
    runs=api('GET','actions/runs?per_page=100')['workflow_runs']
    old=[r['id'] for r in runs if r['head_branch']=='main' and r['head_sha'] not in clean]
    os.environ['OLD_RUN_IDS']=json.dumps(old)
    purge_runs()

def rewrite_remote(repo):
    assert os.environ['GITHUB_REPOSITORY']==REPOSITORY
    expected=os.environ['GITHUB_SHA']
    remote=git(repo,'ls-remote','--heads','--tags','origin').decode().splitlines()
    refs={ref:sha for sha,ref in (line.split() for line in remote)}
    assert set(refs)=={'refs/heads/main','refs/tags/v0.3','refs/tags/v0.4'}, 'Unexpected refs; no history changed'
    assert refs['refs/heads/main']==expected, 'Branch changed; no history changed'
    releases=api('GET','releases')
    assert len(releases)==2 and {r['tag_name'] for r in releases}=={'v0.3','v0.4'}
    asset_digests={r['id']:{a['name']:a.get('digest') for a in r['assets']} for r in releases}
    mapping,replaced=rebuild(repo,refs)
    if not replaced:
        print('Commit identities are private; finishing release references and old run links')
        finish_clean_history(repo)
        return
    runs=api('GET','actions/runs?per_page=100')['workflow_runs']
    old_runs=[r['id'] for r in runs if r['head_sha'] in mapping and r['head_sha']!=mapping[r['head_sha']]]
    assert int(os.environ['GITHUB_RUN_ID']) in old_runs
    args=['push','--atomic']
    args += ['--force-with-lease='+ref+':'+sha for ref,sha in refs.items()]
    args += ['origin']+[mapping[sha]+':'+ref for ref,sha in refs.items()]
    git(repo,*args)
    for release in releases:
        old_target=release['target_commitish']
        if old_target in mapping:
            api('PATCH',f"releases/{release['id']}",{'target_commitish':mapping[old_target]})
        current=api('GET',f"releases/{release['id']}")
        assert asset_digests[release['id']]=={a['name']:a.get('digest') for a in current['assets']}
    # This second run starts from the cleaned commit and removes links to old run heads.
    api('POST','actions/workflows/privacy-cleanup.yml/dispatches',{'ref':'main','inputs':{'phase':'purge','run_ids':json.dumps(old_runs)}})
    print(json.dumps({'commits_rebuilt':len(mapping),'identity_fields_replaced':replaced,'refs_updated':len(refs),'release_assets_unchanged':True}))

def purge_runs():
    ids=json.loads(os.environ.get('OLD_RUN_IDS','[]'))
    assert isinstance(ids,list) and len(ids)<=100
    current=int(os.environ['GITHUB_RUN_ID'])
    for run_id in ids:
        assert isinstance(run_id,int) and run_id>0 and run_id!=current
        for attempt in range(60):
            run=api('GET',f'actions/runs/{run_id}')
            assert run['head_repository']['full_name']==REPOSITORY and run['head_branch']=='main'
            if run['status']=='completed': break
            time.sleep(3)
        else: raise RuntimeError('Earlier run did not finish; nothing deleted for this run')
        api('DELETE',f'actions/runs/{run_id}')
    print(json.dumps({'old_run_links_removed':len(ids)}))
    if ids:
        repo=Path.cwd()
        head=git(repo,'ls-remote','--heads','origin','main').decode().split()[0]
        assert head==os.environ['GITHUB_SHA'], 'Branch changed; cleanup files retained'
        git(repo,'rm','.github/scripts/privacy_cleanup.py','.github/workflows/privacy-cleanup.yml')
        git(repo,'-c','user.name='+OWNER,'-c','user.email='+NOREPLY,'commit','-m','Finish commit email privacy cleanup')
        git(repo,'push','origin','HEAD:refs/heads/main')
        print('Temporary cleanup workflow removed')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--validate',type=Path)
    args=p.parse_args()
    if args.validate:
        refs=dict(line.split(' ',1)[::-1] for line in git(args.validate,'for-each-ref','--format=%(objectname) %(refname)','refs/heads','refs/tags').decode().splitlines())
        mapping,replaced=rebuild(args.validate,refs)
        print(json.dumps({'commits':len(mapping),'identity_fields_replaced':replaced,'file_trees_preserved':True,'all_new_identities_private':True}))
        (args.validate.parent/'privacy-rewrite-plan.json').write_text(json.dumps({'refs':refs,'mapping':mapping,'noreply':NOREPLY},indent=2),encoding='utf-8')
    elif os.environ.get('CLEANUP_PHASE','rewrite')=='purge': purge_runs()
    else: rewrite_remote(Path.cwd())
