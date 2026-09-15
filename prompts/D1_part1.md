# D1 — Recovered user prompts, part 1

Prompt text is preserved verbatim relative to the supplied extraction record.

<a id="d1-u01"></a>

## D1-U01

**Mapped outputs:** `01; C1`  
**Prompt type:** 최초 실행  
**Source-reported status:** 직접 사용 확인  
**SHA-256:** `ebbeef7820a6df2da3758e6cf89020f050441c4a0bbff825fed636f07c4d033c`

```text
# Role & Persona
당신은 의료 분야의 증거기반합성(Evidence-Based Synthesis) 연구를 전공한 박사급 전문가입니다. 체계적 문헌고찰(Systematic Review) 및 메타분석(Meta-Analysis) 방법론과 PRISMA 가이드라인에 대해 최고 수준의 지식과 실무 경험을 보유하고 있습니다.

# Objective
연구자(사용자)의 철저한 지도와 승인 하에, '헬리코박터 파일로리 감염'과 '대장용종'의 연관성에 관한 메타분석 연구를 최초 설계부터 최종 합성까지 단계별로 수행합니다.

# Research Topic & PECO Background
- **Population (대상):** 제한 없음 (일반 인구 집단)
- **Exposure (노출):** 헬리코박터 파일로리 감염 여부 (Helicobacter pylori infection status)
- **Comparison (비교):** 헬리코박터 파일로리 비감염 (Non-infection)
- **Outcome (결과):** 대장용종 발생 (모든 종류의 대장선종 및 양성 대장용종 포함 - All types of colorectal adenomas, benign colorectal polyps)

# Current Task: Step 1 (PubMed Search Strategy)
위의 배경을 바탕으로, PubMed에서 사용할 수 있는 최적의 검색 쿼리(Search Strategy)를 생성해 주세요.
1. 의학주제용어사전인 MeSH Term을 반드시 포함해야 합니다.
2. 누락 없는 검색을 위해 주요 자유어(Title/Abstract keywords, [tiab])를 MeSH와 적절히 조합해야 합니다.
3. 불리언 연산자(AND, OR)를 활용하여 논리적 구조가 명확한 쿼리를 작성해 주세요.

# Critical Constraints (절대 준수 사항)
1. **[인터랙티브 진행]** 이 연구는 100% 연구자(사용자)의 컨펌을 받으며 한 단계씩 진행됩니다. 
2. **[임의 진행 절대 금지]** 이번 답변에서는 오직 **'Step 1: PubMed 검색 쿼리 생성 및 설명'**만 수행해야 합니다. 
3. **[독단적 예측 금지]** 실제 검색을 수행하거나, 문헌의 개수를 예측하거나, 다음 단계(선정/제외 기준 수립 등)로 임의로 넘어가지 마십시오. 쿼리를 보여준 후 반드시 연구자의 피드백을 기다려야 합니다.

# Output Format
답변은 아래의 형식을 엄격히 지켜 작성해 주세요.

1. **PICO 구조화 정의**: 본 연구에 맞게 정리된 PICO 표 또는 리스트
2. **PubMed 검색 쿼리**: PubMed Search Box에 그대로 복사·붙여넣기 할 수 있는 텍스트 형태의 쿼리
3. **쿼리 구성 설명**: 선택한 MeSH Term과 핵심 Keyword들에 대한 간략한 전문가적 분석
4. **승인 요청 메시지**: "연구자님의 확인 및 피드백을 기다리겠습니다. 수정 사항이 없다면 다음 단계로 진행하겠습니다."라는 대기 문구로 답변 마무리
```

<a id="d1-u02"></a>

## D1-U02

**Mapped outputs:** `02; C1`  
**Prompt type:** 최초 실행  
**Source-reported status:** 직접 사용 확인  
**SHA-256:** `9930f4f7184472d0baa03a48cfe10964a2747ba5fca440b9b51161c766737c53`

```text
# Role & Tools
당신은 학술 연구 지원에 특화된 AI 에이전트입니다. 내장된 **Sider Scholar** 및 **SciSpace** 에이전트(플러그인 기능)를 활성화하여, 제공된 쿼리를 바탕으로 **PubMed** 데이터베이스에서 문헌 검색을 수행해 주세요.

# Task
아래의 [PubMed 검색 쿼리]를 사용하여 조건에 부합하는 관련 연구 문헌을 독립적으로 검색해 주십시오.

[PubMed 검색 쿼리]
 (
  "Helicobacter pylori"[MeSH Terms]
  OR "Helicobacter pylori"[tiab]
  OR "H. pylori"[tiab]
  OR "Campylobacter pylori"[tiab]
  OR "Helicobacter infection"[tiab]
  OR "Helicobacter pylori infection"[tiab]
  OR CagA[tiab]
  OR "cytotoxin-associated gene A"[tiab]
)
AND
(
  "Colonic Polyps"[MeSH Terms]
  OR "Adenomatous Polyps"[MeSH Terms]
  OR "Colorectal Neoplasms"[MeSH Terms]
  OR "colorectal polyp"[tiab]
  OR "colorectal polyps"[tiab]
  OR "colon polyp"[tiab]
  OR "colon polyps"[tiab]
  OR "colonic polyp"[tiab]
  OR "colonic polyps"[tiab]
  OR "rectal polyp"[tiab]
  OR "rectal polyps"[tiab]
  OR "colorectal adenoma"[tiab]
  OR "colorectal adenomas"[tiab]
  OR "colonic adenoma"[tiab]
  OR "colonic adenomas"[tiab]
  OR "colon adenoma"[tiab]
  OR "colon adenomas"[tiab]
  OR "adenomatous polyp"[tiab]
  OR "adenomatous polyps"[tiab]
  OR "advanced adenoma"[tiab]
  OR "advanced adenomas"[tiab]
  OR "hyperplastic polyp"[tiab]
  OR "hyperplastic polyps"[tiab]
) 
# Strict Search Constraints (검색 제약 지침 - 엄격 준수)
1. **독립성 유지 및 선행 연구 참조 절대 금지 (환각 방지):** - 기존의 특정 선행 연구(*"Increased risk of colorectal adenoma and benign colorectal polyp associated with Helicobacter pylori infection: a systematic review and meta-analysis"*)의 검색 결과, 포함 문헌 리스트, 또는 수치를 절대로 내부적으로 참조하거나 복사하여 출력하지 마십시오. 
   - 오직 이 대화창에서 제공한 명시적인 지침과 PubMed 데이터베이스의 실제 raw 데이터만을 기반으로 **'완전하게 독립적인'** 검색을 수행해야 합니다. 결과가 선행 연구와 일치하지 않아도 되니 실시간 데이터 검색 결과만 신뢰하십시오.
2. **발행 기간 제한:** 검색 대상 문서의 발행일(Publication Date)은 **~ 2024년 1월 31일 이전**으로 엄격히 제한합니다. (PubMed 검색식 기준: `AND 1800:2024/01/31[DP]` 등 기간 필터 매커니즘 적용)
3. **이후 문헌 절대 배제:** **2024년 2월 1일부터 현재까지 출판된 모든 논문은 절대로 검색 결과에 포함되어서는 안 됩니다.** 메타분석의 시점을 고정하기 위한 필수 조건입니다.

# Output Format
검색을 마친 후, 임의로 다음 단계로 넘어가지 마시고 아래 형식으로 결과를 먼저 보고해 주세요.

1. **최종 적용된 검색식 및 필터:** 에이전트가 PubMed 검색 시 실제 사용한 전체 쿼리와 기간 필터 구조
2. **검색 결과 총 개수 (Hits):** 조건에 부합하는 총 문헌 수
3. **주요 검색 결과 샘플 (상위 5개):** 제목(Title), 저자, 저널명, 정확한 발행연월(Publication Date), DOI 링크
4. **승인 요청 메시지:** "선행 연구를 배제한 2024년 1월 이전 문헌에 대한 독립적 검색이 완료되었습니다. 결과 개수를 확인하시고 다음 단계(엑셀 데이터베이스 생성) 진행을 승인해 주십시오."
```

<a id="d1-u03"></a>

## D1-U03

**Mapped outputs:** `03; C1`  
**Prompt type:** 최초 실행  
**Source-reported status:** 직접 사용 확인  
**SHA-256:** `3a94d94e096ec3df681d4c3dd1bd40d6fe46859e8d1a62100f1be96d375d5b0a`

```text
# Current Task: Step 2 (검색 결과의 CSV 데이터베이스 생성)
이전 단계에서 선행 연구를 배제하고 독립적으로 검색한 총 [※ 653]편의 문헌 목록을 확정합니다. 

이 데이터를 바탕으로, 절대로 새로운 검색을 다시 수행하지 말고 **현재 확보된 문헌 고유의 데이터만을 사용하여 다운로드 가능한 CSV 파일(.csv)**을 생성해 주십시오.

# Execution Rule (파이썬 코드 실행 지침 - 필수)
- 마크다운 표나 텍스트로만 나열하지 마십시오.
- 당신의 **내부 Python 가상 환경(Code Interpreter)**을 반드시 실행하여, 아래 스키마에 맞게 데이터를 데이터프레임으로 구축하고 `to_csv(index=False, encoding='utf-8-sig')` 코드를 사용하여 **실제 다운로드 가능한 유효한 CSV 파일 링크**를 생성하십시오.
- 인코딩은 엑셀에서 열었을 때 한글이나 특수문자가 깨지지 않도록 반드시 `utf-8-sig`를 적용해야 합니다.

# Data Schema (CSV 컬럼 구조)
생성할 CSV 파일은 다음 7개의 열(Column)로 구성되어야 합니다:
1. **ID**: 문헌 식별 번호 (1, 2, 3...)
2. **Publication Year**: 논문 출판 연도 (YYYY 형식)
3. **First Author**: 제1저자명 (성만 표기 또는 Full Name)
4. **All Authors**: 공동 저자를 포함한 전체 저자 리스트 (쉼표로 구분)
5. **Title**: 논문의 전체 제목
6. **Journal**: 게재된 학술지명 (풀네임 또는 공식 약어)
7. **DOI_URL**: 해당 문헌의 DOI 번호 또는 PubMed 상세 페이지 URL

# Constraints (제약 사항)
- **재검색 금지:** 검색을 다시 돌려서 결과 개수가 바뀌거나 문헌 리스트가 변동되어서는 안 됩니다. 이전 단계에서 확인된 문헌 집합만 가공하십시오.
- 파일 작성이 완료되면 임의로 다음 스크리닝 단계로 넘어가지 마십시오.

# Output Format
CSV 파일 생성 작업을 수행한 뒤, 다음과 같이 답변을 마무리해 주세요.

1. **CSV 생성 결과 요약**: 파일에 담긴 총 문헌 개수(N) 재확인 보고
2. **실제 CSV 파일 다운로드 링크** (클릭 시 바로 다운로드되는 링크)
3. **승인 요청 메시지**: "확정된 검색 결과 문헌들을 바탕으로 CSV 데이터베이스 파일 생성이 완료되었습니다. 다운로드 링크를 통해 게재년도, 저자 정보 등이 유실 없이 정확히 반영되었는지 확인해 주십시오. 연구자님의 검토 후 승인이 완료되면, 다음 단계인 [선정/제외 기준에 따른 1차 스크리닝]을 진행하겠습니다."
```

<a id="d1-u04"></a>

## D1-U04

**Mapped outputs:** `04; C1`  
**Prompt type:** 최초 실행  
**Source-reported status:** 직접 사용 확인  
**SHA-256:** `1e042aeca14ffddf48af797d958b6b3a4d0c4bc1cc6ac83f60c4029e35afdbcd`

```text
너는 메타분석 논문의 2단계 title-only screening 보조자다.

현재 입력 데이터는 논문 검색 결과 CSV이며, 제목은 colonic_polyps_meta_result.csv이며, 연결된 구글 드라이브에 업로드되어 있다. 또한 각 행에는 다음 정보만 포함되어 있다:
ID, Publication Year, First Author, All Authors, Title, Journal, DOI_URL

중요:
현재 데이터에는 abstract가 없다. 따라서 제목만으로 명백히 제외 가능한 논문만 Exclude로 판단하고, 조금이라도 관련 가능성이 있거나 판단이 애매한 논문은 Uncertain 또는 Include_fulltext로 남긴다. 이 단계의 목표는 최종 포함 여부 결정이 아니라, full-text 또는 abstract 확인이 필요한 후보를 선별하는 것이다.

연구질문:
Helicobacter pylori infection 또는 H. pylori 관련 gastric pathology가 colorectal polyps, colonic polyps, colorectal adenoma, advanced adenoma, advanced colorectal neoplasia, serrated polyp, colorectal neoplasia와 관련되는지 평가하는 인간 대상 원저 연구를 선별한다.

포함 후보로 남길 논문:
1. 제목에 H. pylori, Helicobacter pylori, CagA, seropositivity, eradication, gastric atrophy, atrophic gastritis, intestinal metaplasia, gastric histopathology 등이 포함되어 있고,
2. 제목에 colorectal polyp, colonic polyp, colon polyp, colorectal adenoma, adenomatous polyp, advanced adenoma, colorectal neoplasia, advanced colorectal neoplasia, serrated polyp, colorectal cancer 등이 포함되어 있으며,
3. 인간 대상 observational study, cohort study, case-control study, cross-sectional study, registry/database study일 가능성이 있는 논문.

판정 원칙:
1. 제목만으로 명백히 무관한 경우만 Exclude한다.
2. colorectal polyp, colon polyp, colorectal adenoma, colorectal neoplasia, advanced colorectal neoplasia가 보이면 우선 Include_fulltext 또는 Uncertain으로 둔다.
3. 제목에 colorectal cancer만 있고 polyp/adenoma 자료가 있는지 불명확하면 Exclude하지 말고 Uncertain으로 둔다.
4. 제목에 gastric polyp 또는 gastric cancer만 있고 colorectal outcome이 전혀 보이지 않으면 Exclude한다.
5. review, systematic review, meta-analysis, umbrella review, guideline, editorial, letter, commentary는 최종 메타분석에는 포함하지 말고 Snowball_only로 둔다.
6. case report, case series, animal study, in vitro study, cell study, molecular mechanism-only study, probiotic/compound experiment는 Exclude한다.
7. 제목에 “association”, “risk”, “prevalence”, “relationship”, “correlation”, “cohort”, “case-control”, “cross-sectional”, “population-based” 등이 있으면 인간 대상 분석 연구일 가능성이 있으므로 보수적으로 남긴다.
8. 확실하지 않으면 Exclude하지 말고 Uncertain으로 둔다.
9. 판단 근거는 반드시 Title에서 확인 가능한 표현만 사용한다. 추정하거나 외부 정보를 만들어내지 않는다.

Stage2_Decision은 아래 4개 중 하나만 사용한다:
- Include_fulltext: 제목만으로 연구질문에 직접 관련된 인간 대상 원저 연구일 가능성이 높아 full text 확인이 필요함
- Uncertain: 관련 가능성은 있으나 제목만으로 포함/제외 판단이 어려움
- Exclude: 제목만으로 연구질문과 명백히 무관하거나 제외 기준에 해당함
- Snowball_only: review, systematic review, meta-analysis 등으로 최종 분석에는 포함하지 않지만 참고문헌 추적에 활용 가능함

Reason_Code는 아래 목록 중 하나만 사용한다:
- likely_relevant_hp_colorectal_polyp
- gastric_pathology_colorectal_outcome
- colorectal_neoplasia_uncertain
- crc_only_uncertain
- gastric_only
- wrong_outcome
- wrong_exposure
- review_or_meta
- case_report
- animal_or_invitro
- mechanistic_only
- unrelated
- unclear

출력 형식:
반드시 CSV 형식으로만 출력한다.
설명문, 요약문, markdown 표는 작성하지 않는다.

출력 컬럼:
ID,Stage2_Decision,Reason_Code,Reason_Short,Evidence_From_Title,Confidence,Next_Action

Confidence는 High, Moderate, Low 중 하나로 작성한다.

Next_Action은 아래 중 하나로 작성한다:
- Retrieve abstract
- Retrieve full text
- Exclude from further screening
- Use for citation chasing
- Human review needed

예시:
ID,Stage2_Decision,Reason_Code,Reason_Short,Evidence_From_Title,Confidence,Next_Action
14,Include_fulltext,likely_relevant_hp_colorectal_polyp,H. pylori와 colorectal polyps의 관련성을 직접 다룸,"Association between Helicobacter pylori infection and colorectal polyps",High,Retrieve full text
34,Snowball_only,review_or_meta,기존 메타분석으로 최종 분석에는 제외하고 참고문헌 추적용으로 사용,"Colorectal cancer risk in East Asian patients with Helicobacter pylori infection: A systematic review and meta-analysis",High,Use for citation chasing
7,Exclude,gastric_only,H. pylori 진단과 위내시경 관련 연구로 colorectal outcome이 제목에 없음,"Simultaneous detection of Helicobacter pylori infection comparing between white light and image-enhanced endoscopy",Moderate,Exclude from further screening

이제 아래에 제공하는 CSV 행들을 위 기준에 따라 스크리닝하라.
```

<a id="d1-u05"></a>

## D1-U05

**Mapped outputs:** `04`  
**Prompt type:** 최초 실행  
**Source-reported status:** 직접 사용 확인  
**SHA-256:** `21e57b185adb2213e84e4ea3a9d01ec666de78bdcfa893b5a95d9e9e5ea9f052`

```text
선정된 논문 리스트만 뽑아서 csv로 만들어서 구글드라이브에 저장해줘
```

<a id="d1-u06"></a>

## D1-U06

**Mapped outputs:** `04; C2`  
**Prompt type:** 배치 재개  
**Source-reported status:** 직접 사용 확인  
**SHA-256:** `31fbef162594de01bab0cd525c51f74de7bcb15063029fa1a54b2cf5944c80d8`

```text
Continue
```

<a id="d1-u07"></a>

## D1-U07

**Mapped outputs:** `04; C3`  
**Prompt type:** 추가 조건  
**Source-reported status:** 관련 있으나 사용 불확실  
**SHA-256:** `6259efbfe1eaa773a2f1a8e134c35c3f4457dd964e40d77338b5ef32c2d87c81`

```text
include_ fulltext로 간주하면 돼
```

<a id="d1-u08"></a>

## D1-U08

**Mapped outputs:** `04; C2`  
**Prompt type:** 배치 재개  
**Source-reported status:** 관련 있으나 사용 불확실  
**SHA-256:** `5f51f6d9ee888eebf994a71c77c33350017eeace3c97568064cb8323e138341a`

```text
I took control of the virtual browser. If you're unsure what changed, ask for more context. If the task is complete, just acknowledge and wrap it up. Otherwise, please proceed.
```

<a id="d1-u09"></a>

## D1-U09

**Mapped outputs:** `04`  
**Prompt type:** 추가 조건  
**Source-reported status:** 관련 있으나 사용 불확실  
**SHA-256:** `49815b1d030c85987ebbfb7a0a90f77cea6d9313336b13e4852c4aa4df8a94b9`

```text
로그인 된 상태야
```

<a id="d1-u10"></a>

## D1-U10

**Mapped outputs:** `04; C3`  
**Prompt type:** 오류 수정  
**Source-reported status:** 직접 사용 확인  
**SHA-256:** `1e1a5be0ce1380faf5abd7f96f4a9193a66589b64a6e1cafaeae2f7e648222e6`

```text
업로드가 안되면 내가 다운로드할 수 있게 해줘
```
