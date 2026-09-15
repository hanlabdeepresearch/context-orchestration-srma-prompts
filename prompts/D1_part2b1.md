# D1 — Recovered user prompts: D1_part2b1

Prompt text is preserved verbatim relative to the supplied extraction record.

<a id="d1-u16"></a>

## D1-U16

**Mapped outputs:** `07; 08; 09; C1; C3`  
**Prompt type:** 정보 보완  
**Source-reported status:** 수정에 사용 확인  
**SHA-256:** `c866213c269b91b963b545ed35e16cdfb7c624f88620da5d23065c740f511109`

```text
너는 에이전트 모드에서 실행되는 메타분석 abstract 보강 및 title/abstract screening reviewer다.

목표:
fulltext_screening_candidates_manual_patch.csv 파일에 포함된 논문들의 PMID, Article Type, Abstract를 보강한 뒤,
title과 abstract를 함께 검토하여 실제 full-text screening 후보를 최종 선별한다.

입력 파일:
fulltext_screening_candidates_manual_patch.csv

중요:
이전 결과에서는 모든 Abstract_Status가 Not_found였다.
따라서 이번 작업의 핵심은 abstract를 최대한 보강하는 것이다.
abstract를 찾지 못한 경우에는 Not_found로 표시하되, 제목상 관련성이 높으면 제외하지 말고 Uncertain_retrieve_fulltext로 남긴다.

연구질문:
Helicobacter pylori infection 또는 H. pylori 관련 gastric pathology가
colorectal polyps, colonic polyps, colorectal adenoma, advanced adenoma,
advanced colorectal neoplasia, serrated polyp, colorectal neoplasia와
관련되는지 평가하는 인간 대상 원저 연구를 선별한다.

작업 절차:
1. 입력 파일을 읽는다.
2. 각 논문에 대해 DOI_URL, Title, Journal, Publication Year를 이용하여 PMID를 찾는다.
3. PubMed 또는 신뢰 가능한 학술 데이터베이스에서 Article Type과 Abstract를 보강한다.
4. Abstract를 찾으면 Abstract_Status를 Found로 표시한다.
5. Abstract를 찾지 못하면 Abstract_Status를 Not_found로 표시한다.
6. Title과 Abstract를 함께 검토하여 Stage2_Abstract_Decision을 새로 판정한다.
7. 전체 결과 파일을 생성한다.
8. Include_for_fulltext 또는 Uncertain_retrieve_fulltext 논문만 추출하여 최종 full-text screening 후보 파일을 생성한다.
9. Exclude 논문은 제외 사유와 함께 별도 파일로 생성한다.
10. Review, meta-analysis, letter, commentary 등은 별도 snowball/article type check 파일로 생성한다.

포함 후보:
1. 인간 대상 original study
2. 연구설계가 cohort, case-control, cross-sectional, retrospective/prospective observational study, registry/database study 중 하나
3. Exposure가 다음 중 하나:
   - H. pylori infection
   - Helicobacter pylori seropositivity
   - CagA 또는 VacA
   - H. pylori eradication
   - gastric atrophy
   - atrophic gastritis
   - intestinal metaplasia
   - gastric histopathology
   - H. pylori-related gastritis
   - precancerous gastric lesion
4. Outcome이 다음 중 하나:
   - colorectal polyp
   - colonic polyp
   - colorectal adenoma
   - adenomatous polyp
   - advanced adenoma
   - advanced colorectal neoplasia
   - colorectal neoplasia
   - serrated polyp
   - sessile serrated lesion
5. 비교군, risk estimate, prevalence comparison, odds ratio, hazard ratio, relative risk, 또는 2x2 table 추출 가능성이 있을 것

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

출력 파일:
1. stage2_title_abstract_screening_results_with_abstracts.csv
   - 전체 입력 논문에 대한 PMID, Article Type, Abstract 보강 및 재판정 결과

2. fulltext_screening_candidates_final.csv
   - Include_for_fulltext, Uncertain_retrieve_fulltext 논문만 포함

3. stage2_abstract_excluded_final.csv
   - Exclude 논문과 제외 사유

4. stage2_snowball_article_check_final.csv
   - Snowball_only, Article_type_check_needed 논문

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
1. 입력 논문 수
2. PMID를 찾은 논문 수
3. abstract를 찾은 논문 수
4. abstract를 찾지 못한 논문 수
5. Stage2_Abstract_Decision 분포
6. 최종 full-text screening 후보 수
7. 제외 논문 수와 주요 제외 사유
8. Snowball/article type check 논문 수
9. 사람이 우선 확인해야 할 논문 ID 목록

주의:
이 단계에서 최종 메타분석 포함 여부를 확정하지 않는다.
애매한 논문은 full text 확인 후보로 남긴다.
abstract가 없다는 이유만으로 제외하지 않는다.
colorectal cancer only 논문은 abstract에서 polyp/adenoma/neoplasia 자료가 확인되지 않으면 제외한다.
gastric polyp only 논문은 colorectal outcome이 없으면 제외한다.
```

<a id="d1-u17"></a>

## D1-U17

**Mapped outputs:** `08; 09; C1; C2`  
**Prompt type:** 정보 보완  
**Source-reported status:** 수정에 사용 확인  
**SHA-256:** `93dff688317479fff9a227d5dd1491be4855ee0d5d484207defd428dfabbc6f5`

```text
너는 에이전트 모드에서 실행되는 메타분석 PMID 및 abstract 보강 보조자다.

목표:
fulltext_screening_candidates_manual_patch.csv 파일에서 아직 PMID와 Abstract가 없는 논문 중
상위 15편만 처리하여 PMID, Article Type, Abstract를 보강한다.

중요:
이번 작업에서는 전체 81편을 한 번에 처리하지 않는다.
반드시 상위 15편만 처리하고 중단한다.
세션 제약을 피하기 위해 batch 단위로 진행한다.

입력 파일:
fulltext_screening_candidates_manual_patch.csv

처리 대상:
1. Abstract_Status가 Found가 아닌 논문
2. 파일 순서 기준 상위 15편

검색 우선순위:
1. DOI_URL이 있으면 DOI로 PubMed 검색
2. DOI 검색 실패 시 Title 전체 문장으로 검색
3. Title 검색 실패 시 First Author + Publication Year + 주요 제목 키워드로 검색
4. PubMed에서 찾지 못하면 Crossref, Europe PMC, publisher page, Google Scholar 등 신뢰 가능한 출처를 보조적으로 확인
5. 그래도 찾지 못하면 Abstract_Status를 Not_found로 둔다

각 논문에 대해 보강할 항목:
- PMID
- Article_Type
- Abstract_Status
- Abstract
- Abstract_Source
- Source_URL 또는 PubMed_URL
- Search_Method
- Search_Result_Status

검색 결과 판정:
1. 제목, 저자, 연도, DOI가 일치하면 Match_confirmed
2. 제목과 저자/연도는 맞지만 DOI가 없으면 Probable_match
3. 유사 제목만 있고 확실하지 않으면 Uncertain_match
4. 찾지 못하면 Not_found

검색 후 screening 판정:
Title과 Abstract를 함께 검토하여 Stage2_Abstract_Decision을 부여한다.

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

출력 파일:
1. abstract_enrichment_batch_01_results.csv
   - 이번 batch 15편의 PMID/abstract 보강 및 screening 결과

2. fulltext_candidates_after_batch_01.csv
   - 기존 후보 파일에 이번 batch 결과를 반영한 누적 파일

3. abstract_enrichment_batch_01_not_found.csv
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
3. abstract를 찾은 논문 수
4. abstract를 찾지 못한 논문 수
5. Stage2_Abstract_Decision 분포
6. Exclude로 바뀐 논문 ID
7. Uncertain으로 남은 논문 ID
8. 다음 batch에서 사용할 입력 파일명

주의:
abstract가 없다는 이유만으로 제외하지 않는다.
검색이 불확실하면 Uncertain_retrieve_fulltext로 둔다.
제목, 저자, 연도, DOI가 일치하지 않으면 match confirmed로 기록하지 않는다.
```

<a id="d1-u18"></a>

## D1-U18

**Mapped outputs:** `08; 09; C1; C2`  
**Prompt type:** 배치 재개  
**Source-reported status:** 수정에 사용 확인  
**SHA-256:** `6fe50a1b4547ad96797cbce00bd28cc1a3e71f3e818d94b43afa06e0df548221`

```text
너는 에이전트 모드에서 실행되는 메타분석 PMID 및 abstract 보강 보조자다.

목표:
fulltext_candidates_after_batch_01.csv 파일에서 아직 Abstract_Status가 Found가 아닌 논문 중
파일 순서 기준 상위 15편만 처리하여 PMID, Article Type, Abstract를 보강하고,
title과 abstract를 함께 검토하여 Stage2_Abstract_Decision을 갱신한다.

중요:
이번 작업은 batch 02이다.
전체 파일을 한 번에 처리하지 않는다.
반드시 Abstract_Status가 Found가 아닌 논문 중 상위 15편만 처리하고 중단한다.
이미 Abstract_Status가 Found인 논문은 수정하지 않는다.
이미 Exclude로 판정된 논문도 수정하지 않는다.

입력 파일:
fulltext_candidates_after_batch_01.csv

처리 대상:
1. Abstract_Status가 Found가 아닌 논문
2. 위 조건을 만족하는 논문 중 파일 순서 기준 상위 15편

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

출력 파일:
1. abstract_enrichment_batch_02_results.csv
   - 이번 batch 15편의 PMID/abstract 보강 및 screening 결과

2. fulltext_candidates_after_batch_02.csv
   - 기존 누적 파일에 이번 batch 결과를 반영한 전체 81편 파일

3. abstract_enrichment_batch_02_not_found.csv
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
3. abstract를 찾은 논문 수
4. abstract를 찾지 못한 논문 수
5. Stage2_Abstract_Decision 분포
6. Exclude로 바뀐 논문 ID
7. Uncertain으로 남은 논문 ID
8. 전체 누적 파일에서 Abstract_Status가 Found인 논문 수
9. 전체 누적 파일에서 아직 Abstract_Status가 Found가 아닌 논문 수
10. 다음 batch에서 사용할 입력 파일명

주의:
abstract가 없다는 이유만으로 제외하지 않는다.
검색이 불확실하면 Uncertain_retrieve_fulltext로 둔다.
제목, 저자, 연도, DOI가 일치하지 않으면 Match_confirmed로 기록하지 않는다.
```
