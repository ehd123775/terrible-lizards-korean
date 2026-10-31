"""Reconstruct a reviewed PAK and synchronize it with the repository."""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import subprocess

PAK='project/terrible_lizards/Content/Paks/zzz_TerribleLizards_Korean_P.pak'

def prepare(root, sync=False):
    meta=json.loads((root/'project/release.json').read_text(encoding='utf-8'))
    path=root/PAK
    data=path.read_bytes()
    target=os.environ.get('GITHUB_SHA','local-verification')
    if hashlib.sha256(data).hexdigest()!=meta['pak_sha256']:
        delta=json.loads((root/'project/build/pak_delta.json').read_text(encoding='utf-8'))
        assert hashlib.sha256(data).hexdigest()==delta['base_sha256'], 'Unexpected base PAK'
        assert delta['target_sha256']==meta['pak_sha256'], 'Delta targets another release'
        chunks=[]
        for op in delta['ops']:
            if 'copy' in op:
                start,size=op['copy']
                assert isinstance(start,int) and isinstance(size,int) and 0<=start<=start+size<=len(data)
                chunks.append(data[start:start+size])
            else:
                chunks.append(base64.b64decode(op['data'],validate=True))
        data=b''.join(chunks)
        assert len(data)==delta['target_size']
        assert hashlib.sha256(data).hexdigest()==meta['pak_sha256'], 'Reconstructed PAK mismatch'
        path.write_bytes(data)
        if sync:
            repo=os.environ['GH_REPO']
            def api(method, endpoint, payload):
                result=subprocess.run(['gh','api','--method',method,f'repos/{repo}/{endpoint}','--input','-'],input=json.dumps(payload),text=True,capture_output=True,check=True)
                return json.loads(result.stdout)
            blob=api('POST','git/blobs',dict(content=base64.b64encode(data).decode('ascii'),encoding='base64'))
            base_tree=subprocess.check_output(['git','rev-parse','HEAD^{tree}'],cwd=root,text=True).strip()
            tree=api('POST','git/trees',dict(base_tree=base_tree,tree=[dict(path=PAK,mode='100644',type='blob',sha=blob['sha'])]))
            commit=api('POST','git/commits',dict(message=f"Update packaged Korean patch {meta['tag']}",tree=tree['sha'],parents=[target]))
            # A concurrent branch change rejects this fast-forward update.
            api('PATCH','git/refs/heads/main',dict(sha=commit['sha'],force=False))
            target=commit['sha']
    return target

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--sync',action='store_true')
    args=parser.parse_args()
    target=prepare(Path.cwd(),args.sync)
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'],'a',encoding='utf-8') as f:
            f.write('target='+target+'\n')
    print('PAK checksum verified')
