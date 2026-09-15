# D1 — Recovered user prompts: D1_part2b2

Prompt text is preserved verbatim relative to the supplied extraction record.

<a id="d1-u19"></a>

## D1-U19

**Mapped outputs:** `08; 09; C1; C2; C3`  
**Prompt type:** 오류 수정  
**Source-reported status:** 수정에 사용 확인  
**SHA-256:** `e0b27c321eb8e2f8b5c9450f916f02b0ad84f9adf422098847186c7c26a01a6e`

```text
너는 에이전트 모드에서 실행되는 메타분석 PMID 및 abstract 보강 보조자다.

목표:
fulltext_candidates_after_batch_01.csv 파일에서 아직 Abstract_Status가 Found가 아닌 논문 중
파일 순서 기준 상위 20편만 처리하여 PMID, Article Type, Abstract를 보강하고,
title과 abstract를 함께 검토하여 Stage2_Abstract_Decision을 갱신한다.

중요:
이번 작업은 batch 02 fixed이다.
이전 batch 02 결과에서는 CSV 컬럼 밀림과 ID/PMID 혼동 문제가 발생했다.
따라서 원본 논문 ID를 절대 변경하지 말고, PMID는 반드시 PMID 컬럼에만 입력한다.
이번 batch에서는 전체 파일을 한 번에 처리하지 않는다.
반드시 Abstract_Status가 Found가 아닌 논문 중 상위 20편만 처리하고 중단한다.

입력 파일:
fulltext_candidates_after_batch_01.csv

처리 대상:
1. Abstract_Status가 Found가 아닌 논문
2. 위 조건을 만족하는 논문 중 파일 순서 기준 상위 20편
3. 이미 Abstract_Status가 Found인 논문은 수정하지 않는다.
4. 이미 Exclude로 판정된 논문은 수정하지 않는다.

검색 우선순위:
1. DOI_URL이 있으면 DOI로 PubMed 검색
2. DOI 검색 실패 시 Title 전체 문장으로 PubMed 검색
3. Title 검색 실패 시 First Author + Publication Year + 주요 제목 키워드로 PubMed 검색
4. PubMed에서 찾지 못하면 Europe PMC, Crossref, publisher page 등 신뢰 가능한 출처를 보조적으로 확인
5. 그래도 찾지 못하면 Abstract_Status를 Not_found로 둔다

검색 결과 판정:
1. 제목, 저자, 연도, DOI가 일치하면 Match_confirmed
2. 제목과 저자/연도는 맞지만 DOI가 없으면 Probable_match
3. 유사 제목만 있고 확실하지 않으면 Uncertain_match
4. 찾지 못하면 Not_found

연구질문:
Helicobacter pylori infection 또는 H. pylori 관련 gastric pathology가
colorectal polyps, colonic polyps, colorectal adenoma, advanced adenoma,
advanced colorectal neoplasia, serrated polyp, colorectal neoplasia와
관련되는지 평가하는 인간 대상 원저 연구를 선별한다.

포함 후보:
1. 인간 대상 original study
2. Exposure가 H. pylori infection, H. pylori seropositivity, CagA/VacA, H. pylori eradication, H. pylori-associated gastritis, gastric atrophy, atrophic gastritis, intestinal metaplasia, gastric histopathology, precancerous gastric lesion 중 하나
3. Outcome이 colorectal polyp, colonic polyp, colorectal adenoma, adenomatous polyp, advanced adenoma, advanced colorectal neoplasia, colorectal neoplasia, serrated polyp, sessile serrated lesion 중 하나
4. 비교군, risk estimate, prevalence comparison, odds ratio, hazard ratio, relative risk, 또는 2x2 table 추출 가능성이 있음

제외:
1. Review, systematic review, meta-analysis, umbrella review, guideline
2. Letter, reply, commentary, editorial
3. Case report 또는 단순 case series
4. Animal, in vitro, cell-line, molecular mechanism-only study
5. Gastric polyp, gastric cancer, upper GI lesion만 다루고 colorectal outcome이 없음
6. Colorectal cancer만 다루고 polyp/adenoma/neoplasia 자료가 명확히 없음
7. H. pylori 또는 gastric pathology exposure가 없음
8. Outcome이 colorectal polyp/adenoma/neoplasia/serrated lesion이 아님
9. 비교군이 전혀 없고 association 분석이 불가능한 경우

Stage2_Abstract_Decision은 아래 중 하나만 사용한다:
- Include_for_fulltext
- Uncertain_retrieve_fulltext
- Exclude
- Snowball_only
- Article_type_check_needed

Reason_Code는 아래 중 하나만 사용한다:
- relevant_hp_colorectal_polyp
- relevant_hp_colorectal_adenoma
- relevant_hp_advanced_neoplasia
- relevant_hp_serrated_polyp
- gastric_pathology_colorectal_outcome
- crc_only_no_polyp_data
- gastric_only_no_colorectal_outcome
- wrong_exposure
- wrong_outcome
- wrong_population
- review_or_meta
- letter_reply_commentary
- case_report
- animal_or_invitro
- mechanistic_only
- no_comparator_likely
- abstract_not_found_uncertain
- unclear_abstract

매우 중요한 파일 작성 규칙:
1. 원본 ID 컬럼에는 반드시 원래 논문 ID를 유지한다.
2. PubMed ID는 PMID 컬럼에만 입력한다.
3. ID와 PMID를 절대 바꾸지 않는다.
4. 모든 출력 행은 동일한 컬럼 수를 가져야 한다.
5. Abstract, Title, Key_Abstract_Evidence, Reviewer_Comment처럼 쉼표가 포함될 수 있는 텍스트 필드는 반드시 큰따옴표로 감싼다.
6. Abstract 안의 줄바꿈은 공백으로 치환한다.
7. Abstract 안의 큰따옴표는 작은따옴표로 바꾸거나 CSV escape 처리한다.
8. CSV 파일이 pandas.read_csv()로 오류 없이 열릴 수 있어야 한다.
9. CSV와 함께 XLSX 파일도 생성한다.
10. 결과 파일 저장 후 다시 읽어서 행 수와 컬럼 수가 정상인지 검증한다.

출력 파일:
1. abstract_enrichment_batch_02_results_fixed.csv
2. fulltext_candidates_after_batch_02_fixed.csv
3. abstract_enrichment_batch_02_not_found_fixed.csv
4. fulltext_candidates_after_batch_02_fixed.xlsx

출력 컬럼:
ID,
Publication Year,
First Author,
Title,
Journal,
DOI_URL,
PMID,
Article_Type,
Abstract_Status,
Abstract,
Abstract_Source,
Source_URL,
Search_Method,
Search_Result_Status,
Stage2_Abstract_Decision,
Reason_Code,
Study_Design_If_Stated,
Exposure_If_Stated,
Outcome_If_Stated,
Comparator_If_Stated,
Key_Abstract_Evidence,
Confidence,
Next_Action,
Reviewer_Comment

작업 완료 후 요약 보고:
1. 이번 batch 입력 논문 수
2. PMID를 찾은 논문 수
3. abstract를 찾은 논문 수
4. abstract를 찾지 못한 논문 수
5. Stage2_Abstract_Decision 분포
6. Exclude로 바뀐 논문 ID
7. Uncertain으로 남은 논문 ID
8. 전체 누적 파일에서 Abstract_Status가 Found인 논문 수
9. 전체 누적 파일에서 아직 Abstract_Status가 Found가 아닌 논문 수
10. CSV 검증 결과: 행 수, 컬럼 수, pandas.read_csv() 성공 여부
11. 다음 batch에서 사용할 입력 파일명

주의:
abstract가 없다는 이유만으로 제외하지 않는다.
검색이 불확실하면 Uncertain_retrieve_fulltext로 둔다.
제목, 저자, 연도, DOI가 일치하지 않으면 Match_confirmed로 기록하지 않는다.
원본 ID를 절대 PMID로 대체하지 않는다.
```

<a id="d1-u20"></a>

## D1-U20

**Mapped outputs:** `08; 09; C1; C2; C3`  
**Prompt type:** 재실행  
**Source-reported status:** 수정에 사용 확인  
**SHA-256:** `1118bfd4c3fc973a5007b7cc4622fba66131c1332f6aab41a04c36cd31e6807c`

```text
너는 에이전트 모드에서 실행되는 메타분석 PMID 및 abstract 보강 보조자다.

목표:
fulltext_candidates_after_batch_01.csv 파일에서 아직 Abstract_Status가 Found가 아닌 논문 중
파일 순서 기준 상위 20편만 처리하여 PMID, Article Type, Abstract를 보강하고,
title과 abstract를 함께 검토하여 Stage2_Abstract_Decision을 갱신한다.

중요:
이번 작업은 batch 02 fixed 재실행이다.
이전 batch 02 결과에서는 CSV 컬럼 밀림 문제가 반복 발생했다.
따라서 이번에는 CSV 파일을 만들지 말고 XLSX 파일만 생성한다.

입력 파일:
fulltext_candidates_after_batch_01.csv

처리 대상:
1. Abstract_Status가 Found가 아닌 논문
2. 위 조건을 만족하는 논문 중 파일 순서 기준 상위 20편
3. 이미 Abstract_Status가 Found인 논문은 수정하지 않는다.
4. 이미 Exclude로 판정된 논문은 수정하지 않는다.

검색 우선순위:
1. DOI_URL이 있으면 DOI로 PubMed 검색
2. DOI 검색 실패 시 Title 전체 문장으로 PubMed 검색
3. Title 검색 실패 시 First Author + Publication Year + 주요 제목 키워드로 PubMed 검색
4. PubMed에서 찾지 못하면 Europe PMC, Crossref, publisher page 등 신뢰 가능한 출처를 보조적으로 확인
5. 그래도 찾지 못하면 Abstract_Status를 Not_found로 둔다.

검색 결과 판정:
1. 제목, 저자, 연도, DOI가 일치하면 Match_confirmed
2. 제목과 저자/연도는 맞지만 DOI가 없으면 Probable_match
3. 유사 제목만 있고 확실하지 않으면 Uncertain_match
4. 찾지 못하면 Not_found

연구질문:
Helicobacter pylori infection 또는 H. pylori 관련 gastric pathology가
colorectal polyps, colonic polyps, colorectal adenoma, advanced adenoma,
advanced colorectal neoplasia, serrated polyp, colorectal neoplasia와
관련되는지 평가하는 인간 대상 원저 연구를 선별한다.

Stage2_Abstract_Decision은 아래 중 하나만 사용한다:
- Include_for_fulltext
- Uncertain_retrieve_fulltext
- Exclude
- Snowball_only
- Article_type_check_needed

Reason_Code는 아래 중 하나만 사용한다:
- relevant_hp_colorectal_polyp
- relevant_hp_colorectal_adenoma
- relevant_hp_advanced_neoplasia
- relevant_hp_serrated_polyp
- gastric_pathology_colorectal_outcome
- crc_only_no_polyp_data
- gastric_only_no_colorectal_outcome
- wrong_exposure
- wrong_outcome
- wrong_population
- review_or_meta
- letter_reply_commentary
- case_report
- animal_or_invitro
- mechanistic_only
- no_comparator_likely
- abstract_not_found_uncertain
- unclear_abstract

매우 중요한 파일 작성 규칙:
1. CSV 파일은 절대 생성하지 않는다.
2. XLSX 파일만 생성한다.
3. 원본 ID 컬럼에는 반드시 원래 논문 ID를 유지한다.
4. PubMed ID는 PMID 컬럼에만 입력한다.
5. ID와 PMID를 절대 바꾸지 않는다.
6. 모든 행은 동일한 컬럼 구조를 가져야 한다.
7. Abstract 안의 줄바꿈은 공백으로 치환한다.
8. Abstract 안의 불필요한 URL fragment나 #:~:text= 같은 브라우저 하이라이트 문자열은 제거한다.
9. 결과 저장 후 다시 XLSX 파일을 열어 행 수와 컬럼 수를 검증한다.
10. 누적 파일은 전체 81행을 유지해야 한다.

출력 파일:
1. abstract_enrichment_batch_02_results_fixed.xlsx
   - 이번 batch 20편의 PMID/abstract 보강 및 screening 결과

2. fulltext_candidates_after_batch_02_fixed.xlsx
   - fulltext_candidates_after_batch_01.csv에 이번 batch 결과를 반영한 전체 81편 누적 파일

3. abstract_enrichment_batch_02_not_found_fixed.xlsx
   - 이번 batch에서 abstract를 찾지 못한 논문

출력 컬럼:
ID,
Publication Year,
First Author,
Title,
Journal,
DOI_URL,
PMID,
Article_Type,
Abstract_Status,
Abstract,
Abstract_Source,
Source_URL,
Search_Method,
Search_Result_Status,
Stage2_Abstract_Decision,
Reason_Code,
Study_Design_If_Stated,
Exposure_If_Stated,
Outcome_If_Stated,
Comparator_If_Stated,
Key_Abstract_Evidence,
Confidence,
Next_Action,
Reviewer_Comment

작업 완료 후 요약 보고:
1. 이번 batch 입력 논문 수
2. PMID를 찾은 논문 수
3. abstract를 찾지 못한 논문 수
4. abstract를 찾지 못한 논문 수
5. Stage2_Abstract_Decision 분포
6. Exclude로 바뀐 논문 ID
7. Uncertain으로 남은 논문 ID
8. 전체 누적 파일에서 Abstract_Status가 Found인 논문 수
9. 전체 누적 파일에서 아직 Abstract_Status가 Found가 아닌 논문 수
10. XLSX 검증 결과: 행 수, 컬럼 수, 파일 재열기 성공 여부
11. 다음 batch에서 사용할 입력 파일명

주의:
abstract가 없다는 이유만으로 제외하지 않는다.
검색이 불확실하면 Uncertain_retrieve_fulltext로 둔다.
제목, 저자, 연도, DOI가 일치하지 않으면 Match_confirmed로 기록하지 않는다.
원본 ID를 절대 PMID로 대체하지 않는다.
```
