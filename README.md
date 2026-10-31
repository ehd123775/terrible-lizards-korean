# Terrible Lizards 한글패치

Xbox PC / WinGDK 버전용 비공식 한국어 패치입니다. 현재 버전은 **v0.6 — 전체 텍스트 4차 검수 수정본**입니다.

## 다운로드

**[최신 한글패치 받기](https://github.com/ehd123775/terrible-lizards-korean/releases/latest)**

릴리스의 **Assets**에서 `TerribleLizards_Korean_v0.6.zip`을 받으세요. 패치는 [Releases](https://github.com/ehd123775/terrible-lizards-korean/releases)에 버전별로 올립니다.

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

## v0.6 검수 내역

| 항목 | 상태 |
| --- | --- |
| 게임 텍스트 | 2,787개 항목 / 중복 제외 2,606개 문자열 전체 처리 |
| 이번 검수 | 전체 한국어 문구 2,606개 정독 / 의심 문구 52개 원문 재대조 |
| 이번 수정 | v0.5 대비 50개 문자열 / 연결된 키 50개 수정 |
| 원문 유지 | 숫자·기호·기술명·브랜드 등 18개 |
| 조작 키 표시 | 엔진 공용 키 이름·조합 표식 362개 별도 처리 |
| 구조 검사 | 키·원문 해시·인덱스·참조 횟수 보존 확인 |
| 누락·서식 | 빈 번역, 버튼 표식, 암호, 태그, 줄바꿈 검사 통과 |
| 패키지 | PAK 재추출 비교 및 ZIP 무결성 검사 통과 |
| 실제 화면 | 이전 v0.3 메뉴·설정 표시 확인 / v0.6 실기 미확인 |

이번에는 메뉴·설정부터 대사·목표·수집품·일지·연구 문서까지 전체 한국어 문구를 빠짐없이 다시 읽었습니다. 의심 문구는 영어 원문과 대조하고 모호한 일부는 원본 일본어 번역도 참고했습니다. 관용어, 수량·비교·조건, 문장 연결과 어색한 직역을 수정했습니다. ‘닭 여러 마리’를 ‘여러 번’으로 옮긴 대사, ‘정황을 맞춰 보면 안다’는 관용어, 인형을 받침대에 놓기 전이라는 소실 조건 등을 바로잡았습니다.

v0.3에서 수정한 **`左 Shift` → `왼쪽 Shift`**와 Ctrl·Alt·방향키·마우스·컨트롤러 키 이름을 그대로 유지합니다. 파일과 문자열 검사를 마쳤으며, 모든 키를 실제 화면에서 확인한 것은 아닙니다.

**전체 챕터 실플레이, 모든 대사의 상황별 말투, 컷신 자막 타이밍과 화면 잘림은 추가 확인 대상입니다.** 앞선 전체 영한 대조에 이어 전체 한국어 문구의 4차 정독과 의심 문구 원문 대조를 마친 베타로 배포합니다. v0.6의 게임 실행과 화면 검증은 진행하지 않았습니다.

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
