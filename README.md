# Terrible Lizards 한글패치

Xbox PC / WinGDK 버전용 비공식 한국어 패치입니다. 현재 버전은 **v0.5 — 3차 집중 검수 수정본**입니다.

## 다운로드

**[최신 한글패치 받기](https://github.com/ehd123775/terrible-lizards-korean/releases/latest)**

릴리스의 **Assets**에서 `TerribleLizards_Korean_v0.5.zip`을 받으세요. 패치는 [Releases](https://github.com/ehd123775/terrible-lizards-korean/releases)에 버전별로 올립니다.

ZIP 안에는 패치 파일 하나만 들어 있습니다.

```text
terrible_lizards/
└─ Content/
   └─ Paks/
      └─ zzz_TerribleLizards_Korean_P.pak
```

## 설치

1. 게임을 완전히 종료합니다.
2. 패치 ZIP의 압축을 풉니다.
3. `terrible_lizards` 폴더를 게임 설치 위치의 **Content** 폴더에 복사합니다. 같은 폴더는 합치고 기존 한글패치 파일은 덮어씁니다.
4. **Options → Accessibility → Text Language**에서 **Japanese**를 선택합니다. 적용되면 해당 항목이 **한국어**로 바뀝니다.
5. **자막을 켜고 저장**합니다.

예시 경로:

```text
D:\xbox\Terrible Lizards\Content\terrible_lizards\Content\Paks\zzz_TerribleLizards_Korean_P.pak
```

일본어 슬롯을 한국어로 대체하는 패치입니다. 원본 게임 PAK·UCAS·UTOC와 저장 데이터는 수정하지 않습니다.

## v0.5 검수 내역

| 항목 | 상태 |
| --- | --- |
| 게임 텍스트 | 2,787개 항목 / 중복 제외 2,606개 문자열 전체 처리 |
| 원문 대조 | 전체 2차 검수 완료 / 이번 3차에서는 중점 문구 589개 재대조 |
| 이번 수정 | v0.4 대비 16개 문자열 / 연결된 키 16개 수정 |
| 원문 유지 | 숫자·기호·기술명·브랜드 등 18개 |
| 조작 키 표시 | 엔진 공용 키 이름·조합 표식 362개 별도 처리 |
| 구조 검사 | 키·원문 해시·인덱스·참조 횟수 보존 확인 |
| 누락·서식 | 빈 번역, 버튼 표식, 암호, 태그, 줄바꿈 검사 통과 |
| 패키지 | PAK 재추출 비교 및 ZIP 무결성 검사 통과 |
| 실제 화면 | 이전 v0.3 메뉴·설정 표시 확인 / v0.5 실기 미확인 |

3차 집중 검수에서는 수량·부정·조건 표현, 목표·조작 안내와 관련 대사·문서를 다시 살폈습니다. ‘한 마리보다 많다’의 수량 의미, 시설 퇴거 규정, 사물 이동과 가지에 매달려 흔드는 동작을 명확히 했습니다. 원문에 없는 호칭을 걷어내고 반복 대사 누락, 문서의 직역과 오탈자도 수정했습니다. 전체 2,606개 문자열에 대한 파일 검사를 다시 통과했습니다.

v0.3에서 수정한 **`左 Shift` → `왼쪽 Shift`**와 Ctrl·Alt·방향키·마우스·컨트롤러 키 이름을 그대로 유지합니다. 파일과 문자열 검사를 마쳤으며, 모든 키를 실제 화면에서 확인한 것은 아닙니다.

**전체 챕터 실플레이, 모든 대사의 상황별 말투, 컷신 자막 타이밍과 화면 잘림은 추가 확인 대상입니다.** 전체 텍스트의 2차 검수와 중점 문구의 3차 집중 검수를 마친 베타로 배포합니다. v0.5의 게임 실행과 화면 검증은 진행하지 않았습니다.

자세한 결과는 [검수 보고서](project/docs/REVIEW.md), 버전별 변경은 [변경 기록](CHANGELOG.md)에서 확인하세요. `project/docs/review_changes.json`에는 스토리를 포함한 원문과 수정 전후 문장이 있습니다.

## 포함 범위와 지원 버전

- 메뉴·설정·튜토리얼·목표·아이템 설명·대사 자막·녹취록·일지·편지·연구 및 군사 문서·게임 언어 리소스의 제작진 직책과 안내문
- 한국어 글꼴과 공용 조작 키 이름
- **Xbox PC / WinGDK**, 게임 프로젝트 버전 `v0.3.24+2233f6e` 기준
- Steam판 및 이후 업데이트와의 호환성은 확인하지 않았습니다.

영상·이미지·3D 모델에 직접 들어간 글자, 음성 더빙, 온라인 소식 카드 같은 외부 문구, 조작 키 이외의 엔진·Xbox 공용 시스템 문구는 범위에 포함하지 않습니다.

## 업데이트와 제거

- 업데이트: 게임 종료 후 Releases의 새 패치 파일을 같은 위치에 덮어씁니다.
- 제거: 게임 종료 후 `zzz_TerribleLizards_Korean_P.pak` 파일 하나를 삭제하고 원하는 언어를 다시 선택합니다.
- `~mods` 등 다른 폴더에 예전 패치가 있다면 한 버전만 남겨 중복을 피하세요.
- 글꼴 교체는 다른 언어의 화면 모양에도 영향을 줄 수 있습니다.

## 문제 제보

[Issues](https://github.com/ehd123775/terrible-lizards-korean/issues)에 게임·패치 버전, 발생 위치와 문제 문구를 적어 주세요. 화면이 있으면 확인에 도움이 됩니다. 스토리 관련 제보에는 스포일러 표시를 붙여 주세요.

## 글꼴 및 도구

Noto Sans KR / Source 계열 글꼴: © 2014–2021 Adobe. SIL Open Font License 1.1. [라이선스 전문](project/licenses/NotoSans-OFL.txt)은 패치 PAK 내부에도 포함되어 있습니다.

패키징: [repak](https://github.com/trumank/repak). 리소스 구조 참고: [CUE4Parse](https://github.com/FabianFG/CUE4Parse/blob/master/CUE4Parse/UE4/Localization/FTextLocalizationResource.cs).

게임 개발사·배급사 및 Microsoft와 관계없는 비공식 패치입니다.
