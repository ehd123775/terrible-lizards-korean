# Terrible Lizards 한글패치 v0.2

Xbox PC / WinGDK 버전용 비공식 한국어 패치입니다. 게임 언어 리소스 전체를 번역한 베타 버전이며, 실제 플레이 화면 검수는 아직 진행하지 않았습니다.

**[한글패치 v0.2 다운로드](https://github.com/ehd123775/terrible-lizards-korean/raw/refs/heads/main/downloads/TerribleLizards_Korean_v0.2_Copy.zip)**

다운로드 ZIP에는 `terrible_lizards` 폴더와 그 안의 패치 PAK 파일 하나만 들어 있습니다. 설치 설명과 변경 기록은 이 GitHub 페이지에서 확인할 수 있습니다.

## 설치 — 파일 복사만으로 적용

1. 게임을 완전히 종료합니다.
2. 패치 ZIP의 압축을 풉니다.
3. 압축 안의 **terrible_lizards** 폴더를 게임 설치 위치의 **Content** 폴더에 복사합니다. 같은 이름의 폴더는 합치고, 기존 한글패치 파일이 있으면 덮어씁니다.
4. 게임을 실행하고 **Options → Accessibility → Text Language → Japanese**를 선택한 뒤 저장합니다. 적용 후에는 해당 언어가 **한국어 (시험 패치)**로 표시됩니다.
5. **Subtitles**를 켭니다. 언어가 바로 반영되지 않으면 게임을 종료하고 다시 실행합니다.

설치 후에는 다음과 같은 구조가 됩니다.

```text
Content/
└─ terrible_lizards/
   └─ Content/
      └─ Paks/
         ├─ terrible_lizards-WinGDK.pak      ← 원본, 그대로 유지
         ├─ terrible_lizards-WinGDK.utoc     ← 원본, 그대로 유지
         ├─ terrible_lizards-WinGDK.ucas     ← 원본, 그대로 유지
         └─ zzz_TerribleLizards_Korean_P.pak ← 이 패치 파일
```

CMD, PowerShell, 별도 설치 프로그램은 필요하지 않습니다. 한국어를 별도 언어로 추가하는 방식이 아니라 **일본어 슬롯을 한국어로 대체**합니다. 원본 게임 묶음과 저장 데이터는 수정하지 않습니다.

## 지원 버전

- Xbox PC / WinGDK
- 게임 프로젝트 버전: `v0.3.24+2233f6e`
- Unreal Engine 프로젝트 연결 버전: 5.4
- Steam판 및 이후 게임 업데이트와의 호환성은 확인하지 않았습니다.

## 번역 범위

- `Game.locres`의 **2,787개 항목 / 중복 제외 2,606개 문자열 전부 처리**
- 2,588개 문자열 번역, 숫자·기호·기술명·브랜드 표기 등 18개는 의도적으로 유지
- 메뉴, 설정, 튜토리얼, 목표, 아이템 설명, 대사 자막, 녹취록, 일지, 편지, 연구·군사 문서, 게임 언어 리소스에 포함된 제작진 직책 및 안내문 포함
- 게임에 포함된 Noto Sans KR 글꼴을 이용해 주요 UI와 자막용 글꼴 6개 경로 교체

**범위 밖:** 영상에 직접 들어간 글자, 이미지·3D 모델에 그려진 글자, 음성 더빙, 엔진·Xbox 플랫폼의 공용 시스템 문구. 리소스에서 별도로 제공되는 영상 대사는 자막 번역에 포함되지만, 영상 자체를 편집한 것은 아닙니다.

## 검증 상태

- 전체 키, 원문 해시, 문자열 인덱스, 참조 횟수 보존
- 누락·빈 번역 0개
- 암호, 버튼 치환 표식, 서식 태그, 문단 구분 검사
- 사용한 한글 952종의 글꼴 포함 여부 확인
- 생성한 PAK의 파일 8개를 다시 추출하여 제작 데이터와 바이트 단위 비교 통과

**실제 게임에서의 로딩, 줄바꿈, 글자 잘림, 컷신 자막 동기화, 전체 진행은 미검증입니다.** 문맥상 어색한 표현과 고유명사는 추가 검수가 필요할 수 있습니다. 현재 버전은 완성 번역 초안을 담은 베타로 취급해 주세요.

## 업데이트와 제거

- 업데이트: 게임 종료 후 새 패치의 같은 파일을 덮어씁니다. v0.1과 같은 이름을 사용하므로 두 버전을 함께 둘 필요가 없습니다.
- 제거: 게임을 종료하고 `Paks/zzz_TerribleLizards_Korean_P.pak` 파일 하나를 삭제합니다. 게임에서 원하는 언어를 다시 선택하세요.
- 여러 폴더에 패치 파일을 중복 설치하면 충돌할 수 있습니다. 이전 파일이 `~mods` 등에 있다면 한 버전만 남겨 주세요.
- 글꼴 교체는 다른 언어의 화면 모양에도 영향을 줄 수 있습니다.

## 문제 제보

게임 버전, 문제 위치, 원문 또는 표시 문구, 가능하면 화면을 함께 알려 주세요. 스토리 관련 제보에는 스포일러 표시를 붙여 주세요. 세이브 파일이나 개인정보는 올리지 않아도 됩니다.

## 글꼴 및 도구

Noto Sans KR / Source 계열 글꼴: © 2014–2021 Adobe. SIL Open Font License 1.1. 전문은 저장소의 `licenses/NotoSans-OFL.txt`에 있으며, 패치 PAK 내부에도 포함되어 있습니다. 폰트의 내부 데이터는 수정하지 않았습니다.

패키징: [repak](https://github.com/trumank/repak). 리소스 구조 참고: [CUE4Parse](https://github.com/FabianFG/CUE4Parse/blob/master/CUE4Parse/UE4/Localization/FTextLocalizationResource.cs).

본 패치는 게임 개발사·배급사 및 Microsoft와 관계없는 비공식 패치입니다. 게임 실행 파일, 원본 UCAS/UTOC, 영상, 음성은 포함하지 않습니다.
