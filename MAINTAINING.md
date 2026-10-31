# 이후 버전 배포

다운로드는 GitHub Releases를 기준으로 합니다.

새 버전을 준비할 때 PAK, manifest와 SHA256SUMS, 번역·검수 자료, README·CHANGELOG·RELEASE_NOTES를 갱신하고 `release.json`에 새 태그와 ZIP 이름, PAK 해시를 적습니다.

main에 `release.json`이 변경되면 Publish Korean patch release 작업이 실행됩니다. PAK 해시를 검사하고 패치 폴더만 담은 ZIP과 SHA-256 파일을 만든 뒤 해당 태그의 Release에 첨부합니다. Actions 화면의 Run workflow로 다시 실행할 수도 있습니다.

새 수정본에는 새 버전 태그를 사용합니다. `prerelease`는 실제 검증 상태에 맞춰 설정합니다. 현재 v0.3은 전체 진행 검수 전이므로 베타입니다.

게시 후 공개 ZIP을 내려받아 SHA-256과 내부 경로를 확인합니다.
