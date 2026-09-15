# D1 — Recovered user prompts: D1_part3a2

Prompt text is preserved verbatim relative to the supplied extraction record.

<a id="d1-u23"></a>

## D1-U23

**Mapped outputs:** `08; 09; C1; C2; C3`  
**Prompt type:** 재실행  
**Source-reported status:** 관련 있으나 사용 불확실  
**SHA-256:** `f022ad79ce2da7e09a724feb3aef6faab4de8fb864125d75bab98c91600374ff`

```text
너는 에이전트 모드에서 실행되는 메타분석 PMID 및 abstract 보강 보조자다.

목표:
fulltext_candidates_after_batch_03.xlsx 파일에서 아직 Abstract_Status가 Found가 아닌 논문을 모두 처리하여
PMID, Article Type, Abstract를 보강하고,
title과 abstract를 함께 검토하여 Stage2_Abstract_Decision을 최종 갱신한다.

중요:
이번 작업은 batch 04이며, abstract 보강의 마지막 batch이다.
CSV 파일은 생성하지 말고 XLSX 파일만 생성한다.
Abstract_Status가 Found가 아닌 남은 논문 전체를 처리한다.
이미 Abstract_Status가 Found인 논문은 수정하지 않는다.
이미 Exclude로 판정된 논문도 수정하지 않는다.
원본 논문 ID는 절대 변경하지 말고, PMID는 반드시 PMID 컬럼에만 입력한다.
누적 파일은 반드시 전체 81행을 유지해야 한다.

입력 파일:
fulltext_candidates_after_batch_03.xlsx

처리 대상:

1. Abstract_Status가 Found가 아닌 모든 논문
2. 이미 Abstract_Status가 Found인 논문은 수정하지 않는다.
3. 이미 Exclude로 판정된 논문은 수정하지 않는다.

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

* Include_for_fulltext
* Uncertain_retrieve_fulltext
* Exclude
* Snowball_only
* Article_type_check_needed

Reason_Code는 아래 중 하나만 사용한다:

* relevant_hp_colorectal_polyp
* relevant_hp_colorectal_adenoma
* relevant_hp_advanced_neoplasia
* relevant_hp_serrated_polyp
* gastric_pathology_colorectal_outcome
* crc_only_no_polyp_data
* gastric_only_no_colorectal_outcome
* wrong_exposure
* wrong_outcome
* wrong_population
* review_or_meta
* letter_reply_commentary
* case_report
* animal_or_invitro
* mechanistic_only
* no_comparator_likely
* abstract_not_found_uncertain
* unclear_abstract

파일 작성 규칙:

1. CSV 파일은 생성하지 않는다.
2. XLSX 파일만 생성한다.
3. 원본 ID 컬럼에는 반드시 원래 논문 ID를 유지한다.
4. PubMed ID는 PMID 컬럼에만 입력한다.
5. ID와 PMID를 절대 바꾸지 않는다.
6. 모든 행은 동일한 컬럼 구조를 가져야 한다.
7. Abstract 안의 줄바꿈은 공백으로 치환한다.
8. 결과 저장 후 다시 XLSX 파일을 열어 행 수와 컬럼 수를 검증한다.
9. 누적 파일은 전체 81행을 유지해야 한다.

출력 파일:

1. abstract_enrichment_batch_04_results.xlsx

   * 이번 batch의 PMID/abstract 보강 및 screening 결과

2. fulltext_candidates_after_batch_04_final.xlsx

   * fulltext_candidates_after_batch_03.xlsx에 이번 batch 결과를 반영한 전체 81편 최종 누적 파일

3. abstract_enrichment_batch_04_not_found.xlsx

   * 이번 batch에서 abstract를 찾지 못한 논문

4. stage2_abstract_screening_final_included_for_fulltext.xlsx

   * Stage2_Abstract_Decision이 Include_for_fulltext 또는 Uncertain_retrieve_fulltext인 논문만 포함

5. stage2_abstract_screening_final_excluded.xlsx

   * Stage2_Abstract_Decision이 Exclude인 논문만 포함

6. stage2_abstract_screening_final_article_check.xlsx

   * Stage2_Abstract_Decision이 Article_type_check_needed 또는 Snowball_only인 논문만 포함

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
5. 최종 전체 81편의 Abstract_Status 분포
6. 최종 Stage2_Abstract_Decision 분포
7. 최종 full-text screening 후보 수
8. 최종 Exclude 논문 수
9. Article_type_check 또는 Snowball_only 논문 수
10. 아직 Abstract_Status가 Not_found인 논문 ID
11. 사람이 우선 확인해야 할 논문 ID 목록
12. XLSX 검증 결과: 행 수, 컬럼 수, 파일 재열기 성공 여부
13. 3차 full-text screening에 사용할 파일명

주의:
abstract가 없다는 이유만으로 제외하지 않는다.
검색이 불확실하면 Uncertain_retrieve_fulltext로 둔다.
제목, 저자, 연도, DOI가 일치하지 않으면 Match_confirmed로 기록하지 않는다.
원본 ID를 절대 PMID로 대체하지 않는다.
```

<a id="d1-u24"></a>

## D1-U24

**Mapped outputs:** `08; 09; C1; C2; C3`  
**Prompt type:** 재실행  
**Source-reported status:** 관련 있으나 사용 불확실  
**SHA-256:** `f022ad79ce2da7e09a724feb3aef6faab4de8fb864125d75bab98c91600374ff`

```text
너는 에이전트 모드에서 실행되는 메타분석 PMID 및 abstract 보강 보조자다.

목표:
fulltext_candidates_after_batch_03.xlsx 파일에서 아직 Abstract_Status가 Found가 아닌 논문을 모두 처리하여
PMID, Article Type, Abstract를 보강하고,
title과 abstract를 함께 검토하여 Stage2_Abstract_Decision을 최종 갱신한다.

중요:
이번 작업은 batch 04이며, abstract 보강의 마지막 batch이다.
CSV 파일은 생성하지 말고 XLSX 파일만 생성한다.
Abstract_Status가 Found가 아닌 남은 논문 전체를 처리한다.
이미 Abstract_Status가 Found인 논문은 수정하지 않는다.
이미 Exclude로 판정된 논문도 수정하지 않는다.
원본 논문 ID는 절대 변경하지 말고, PMID는 반드시 PMID 컬럼에만 입력한다.
누적 파일은 반드시 전체 81행을 유지해야 한다.

입력 파일:
fulltext_candidates_after_batch_03.xlsx

처리 대상:

1. Abstract_Status가 Found가 아닌 모든 논문
2. 이미 Abstract_Status가 Found인 논문은 수정하지 않는다.
3. 이미 Exclude로 판정된 논문은 수정하지 않는다.

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

* Include_for_fulltext
* Uncertain_retrieve_fulltext
* Exclude
* Snowball_only
* Article_type_check_needed

Reason_Code는 아래 중 하나만 사용한다:

* relevant_hp_colorectal_polyp
* relevant_hp_colorectal_adenoma
* relevant_hp_advanced_neoplasia
* relevant_hp_serrated_polyp
* gastric_pathology_colorectal_outcome
* crc_only_no_polyp_data
* gastric_only_no_colorectal_outcome
* wrong_exposure
* wrong_outcome
* wrong_population
* review_or_meta
* letter_reply_commentary
* case_report
* animal_or_invitro
* mechanistic_only
* no_comparator_likely
* abstract_not_found_uncertain
* unclear_abstract

파일 작성 규칙:

1. CSV 파일은 생성하지 않는다.
2. XLSX 파일만 생성한다.
3. 원본 ID 컬럼에는 반드시 원래 논문 ID를 유지한다.
4. PubMed ID는 PMID 컬럼에만 입력한다.
5. ID와 PMID를 절대 바꾸지 않는다.
6. 모든 행은 동일한 컬럼 구조를 가져야 한다.
7. Abstract 안의 줄바꿈은 공백으로 치환한다.
8. 결과 저장 후 다시 XLSX 파일을 열어 행 수와 컬럼 수를 검증한다.
9. 누적 파일은 전체 81행을 유지해야 한다.

출력 파일:

1. abstract_enrichment_batch_04_results.xlsx

   * 이번 batch의 PMID/abstract 보강 및 screening 결과

2. fulltext_candidates_after_batch_04_final.xlsx

   * fulltext_candidates_after_batch_03.xlsx에 이번 batch 결과를 반영한 전체 81편 최종 누적 파일

3. abstract_enrichment_batch_04_not_found.xlsx

   * 이번 batch에서 abstract를 찾지 못한 논문

4. stage2_abstract_screening_final_included_for_fulltext.xlsx

   * Stage2_Abstract_Decision이 Include_for_fulltext 또는 Uncertain_retrieve_fulltext인 논문만 포함

5. stage2_abstract_screening_final_excluded.xlsx

   * Stage2_Abstract_Decision이 Exclude인 논문만 포함

6. stage2_abstract_screening_final_article_check.xlsx

   * Stage2_Abstract_Decision이 Article_type_check_needed 또는 Snowball_only인 논문만 포함

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
5. 최종 전체 81편의 Abstract_Status 분포
6. 최종 Stage2_Abstract_Decision 분포
7. 최종 full-text screening 후보 수
8. 최종 Exclude 논문 수
9. Article_type_check 또는 Snowball_only 논문 수
10. 아직 Abstract_Status가 Not_found인 논문 ID
11. 사람이 우선 확인해야 할 논문 ID 목록
12. XLSX 검증 결과: 행 수, 컬럼 수, 파일 재열기 성공 여부
13. 3차 full-text screening에 사용할 파일명

주의:
abstract가 없다는 이유만으로 제외하지 않는다.
검색이 불확실하면 Uncertain_retrieve_fulltext로 둔다.
제목, 저자, 연도, DOI가 일치하지 않으면 Match_confirmed로 기록하지 않는다.
원본 ID를 절대 PMID로 대체하지 않는다.
```
