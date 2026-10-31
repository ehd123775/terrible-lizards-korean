# 이후 버전 배포

다운로드는 GitHub Releases를 기준으로 합니다.

관리 자료는 `project/` 폴더에 모아 둡니다. 저장소 첫 화면의 README와 CHANGELOG는 이용자 안내용입니다.

새 버전을 준비할 때 `project/` 안의 PAK, manifest와 SHA256SUMS, 번역·검수 자료와 RELEASE_NOTES, 저장소 첫 화면의 README·CHANGELOG를 갱신하고 `project/release.json`에 새 태그와 ZIP 이름, PAK 해시를 적습니다.

main에 `project/release.json`이 변경되면 Publish Korean patch release 작업이 실행됩니다. `project/terrible_lizards/`의 PAK 해시를 검사하고 ZIP의 최상위에는 `terrible_lizards/` 폴더만 담습니다. ZIP과 SHA-256 파일을 해당 태그의 Release에 첨부합니다. Actions 화면의 Run workflow로 다시 실행할 수도 있습니다.

새 수정본에는 새 버전 태그를 사용합니다. 저장소 오른쪽의 Releases에 최신 다운로드를 표시하려면 `prerelease`를 `false`로 설정합니다. 현재 v0.3은 Latest로 게시하되 제목과 본문에 베타임을 명시합니다. 전체 진행 검수 상태는 README와 릴리스 설명에 별도로 기록합니다.

게시 후 공개 ZIP을 내려받아 SHA-256과 내부 경로를 확인합니다.
