# D1 — Recovered user prompts: D1 part2a

Prompt text is preserved verbatim relative to the supplied extraction record.

<a id="d1-u11"></a>

## D1-U11

**Mapped outputs:** `04; C3`  
**Prompt type:** 재실행  
**Source-reported status:** 수정에 사용 확인  
**SHA-256:** `004f80c901773f8ba513b12ca30dd075621664a15926c5a3f22e09c3c927bf28`

```text
selected_papers.csv 를 만들어서 내가 다운로드할 수 있게 해달라고
```

<a id="d1-u12"></a>

## D1-U12

**Mapped outputs:** `05; 06; C1; C3`  
**Prompt type:** 재검토  
**Source-reported status:** 관련 있으나 사용 불확실  
**SHA-256:** `fcd9d76ba212d300f46a36c6129c090e06ff22f579e7d7e276322b07771a9cc0`

```text
너는 메타분석 title-only screening 결과의 품질 감사자다.

연구질문:
Helicobacter pylori infection 또는 H. pylori 관련 gastric pathology가 colorectal polyps, colonic polyps, colorectal adenoma, advanced adenoma, advanced colorectal neoplasia, serrated polyp, colorectal neoplasia와 관련되는지 평가하는 인간 대상 원저 연구를 선별한다.

입력으로 다음 컬럼을 제공한다:
ID, Publication Year, First Author, Title, Original_Decision, Original_Reason_Code, Original_Confidence, Original_Next_Action, Audit_Category, Audit_Priority, Audit_Comment

작업 목표:
기존 title-only screening 결과에서 false positive와 false negative를 줄이고, 다음 abstract screening으로 넘길 대상을 보정한다.

중요 원칙:
1. 이 단계는 여전히 title-only audit이다. abstract나 full text 내용을 추정하지 않는다.
2. 제목만으로 명백히 무관한 경우만 Exclude한다.
3. 조금이라도 관련 가능성이 있으면 Exclude하지 말고 Uncertain_for_abstract_screening으로 둔다.
4. selected_papers에 포함되었더라도 제목상 gastric polyp/gastric hyperplastic polyp/gastric adenoma만 다루고 colorectal outcome이 없으면 Exclude 또는 Downgrade한다.
5. Exclude로 되어 있더라도 제목에 H. pylori, Helicobacter pylori, HP, CagA, VacA, eradication, atrophic gastritis, gastric atrophy, intestinal metaplasia 등이 보이고, 동시에 colorectal polyp, colon polyp, colorectal adenoma, advanced adenoma, colorectal neoplasia, serrated polyp 등이 보이면 Rescue한다.
6. Review, systematic review, meta-analysis, guideline, letter, reply, editorial, commentary는 최종 정량분석에 포함하지 말고 Snowball_only 또는 Exclude_article_type으로 둔다.
7. case report는 Exclude한다. 단, 제목만으로 case report인지 확실하지 않으면 Uncertain으로 둔다.
8. animal_or_invitro reason code가 붙어 있더라도 제목에 retrospective study, cohort, cross-sectional, patient, population, hospital, colonoscopy 같은 인간 연구 단서가 있으면 제외 사유를 반드시 재검토한다.
9. 판단 근거는 반드시 제목에서 확인 가능한 표현만 사용한다.

Corrected_Decision은 아래 중 하나만 사용한다:
- Include_for_abstract_screening
- Uncertain_for_abstract_screening
- Exclude
- Snowball_only
- Article_type_check_needed

Corrected_Reason_Code는 아래 중 하나만 사용한다:
- likely_relevant_hp_colorectal_polyp
- gastric_pathology_colorectal_outcome
- serrated_polyp_relevant
- crc_only_uncertain
- colorectal_neoplasia_uncertain
- gastric_only_no_colorectal_outcome
- wrong_exposure
- wrong_outcome
- review_or_meta
- letter_reply_commentary
- case_report
- animal_or_invitro
- mechanistic_only
- unrelated
- unclear_title_only

출력 형식:
반드시 CSV 형식으로만 출력한다.
설명문, markdown 표, 요약문은 쓰지 않는다.

출력 컬럼:
ID,Original_Decision,Corrected_Decision,Corrected_Reason_Code,Correction_Type,Corrected_Next_Action,Title_Evidence,Reviewer_Comment,Confidence

Correction_Type은 아래 중 하나만 사용한다:
- Keep_original
- Downgrade_include
- Rescue_exclude
- Recode_reason
- Keep_uncertain
- Keep_snowball

Corrected_Next_Action은 아래 중 하나만 사용한다:
- Retrieve abstract
- Exclude from further screening
- Use for citation chasing
- Check article type
- Human review needed
```

<a id="d1-u13"></a>

## D1-U13

**Mapped outputs:** `05; 06; C1; C3`  
**Prompt type:** 재검토  
**Source-reported status:** 수정에 사용 확인  
**SHA-256:** `f0edfa8b116e59205c4d153559d62f860e6fa65408a0691c38dc8451ea22b975`

```text
너는 에이전트 모드에서 실행되는 메타분석 스크리닝 품질 감사자다.

목표:
이전 단계에서 생성된 title-only screening 결과 파일을 검토하여,
잘못 포함된 논문(false positive)과 잘못 제외된 논문(false negative)을 보정하고,
다음 단계인 abstract screening에 사용할 후보군 CSV 파일을 새로 생성한다.

입력 파일:
1. title_screening_stage2_results_v2.csv
   - 이전 title-only screening 전체 결과
2. selected_papers.csv
   - Stage2_Decision = Include_fulltext만 추출한 파일
3. stage2_title_screening_audit_flags.csv
   - 기존 결과에 대해 감사 플래그가 붙은 파일
4. colonicpolyps_search.csv
   - 원본 검색 결과 전체 파일

중요:
selected_papers.csv는 Include_fulltext만 포함하므로 그대로 다음 단계에 사용하지 않는다.
Uncertain 논문과 rescue가 필요한 Exclude 논문도 함께 검토해야 한다.

연구질문:
Helicobacter pylori infection 또는 H. pylori 관련 gastric pathology가
colorectal polyps, colonic polyps, colorectal adenoma, advanced adenoma,
advanced colorectal neoplasia, serrated polyp, colorectal neoplasia와
관련되는지 평가하는 인간 대상 원저 연구를 선별한다.

스크리닝 원칙:
1. 이 단계는 title-only audit이다.
2. abstract나 full text 내용을 추정하지 않는다.
3. 제목만으로 명백히 무관한 경우만 Exclude한다.
4. 조금이라도 관련 가능성이 있으면 Exclude하지 말고 abstract screening 후보로 남긴다.
5. 제목에 colorectal polyp, colon polyp, colorectal adenoma, advanced adenoma, colorectal neoplasia, serrated polyp이 보이면 우선 후보로 남긴다.
6. 제목에 colorectal cancer만 있고 polyp/adenoma 자료 여부가 불분명하면 Exclude하지 말고 Uncertain으로 둔다.
7. 제목에 gastric polyp, gastric hyperplastic polyp, gastric adenoma, gastric cancer만 있고 colorectal outcome이 없으면 Exclude한다.
8. H. pylori 또는 gastric pathology exposure가 없으면 Exclude한다.
9. review, systematic review, meta-analysis, umbrella review는 최종 분석에는 포함하지 않고 Snowball_only로 분류한다.
10. letter, reply, commentary, editorial은 Article_type_check_needed 또는 Exclude로 분류한다.
11. case report는 Exclude한다.
12. animal, in vitro, cell-line, molecular mechanism-only study는 Exclude한다.
13. 기존 Reason_Code가 animal_or_invitro로 되어 있어도 제목에 retrospective study, cohort, cross-sectional, patients, population, hospital, colonoscopy 등이 보이면 반드시 재검토한다.
14. 판단 근거는 반드시 Title에서 확인 가능한 표현만 사용한다.

특히 반드시 재검토할 항목:
- 현재 Include_fulltext이지만 gastric polyp/gastric hyperplastic polyp/gastric adenoma 단독으로 보이는 논문
- 현재 Exclude이지만 H. pylori 또는 gastric pathology와 colorectal polyp/adenoma/neoplasia가 함께 제목에 보이는 논문
- Reason_Code가 animal_or_invitro인데 제목상 인간 대상 연구로 보이는 논문
- review/meta-analysis/letter/reply/commentary로 보이는 논문

보정 판정값:
Corrected_Decision은 아래 중 하나만 사용한다.

1. Include_for_abstract_screening
   - 제목상 연구질문과 직접 관련될 가능성이 높아 abstract 확인이 필요함

2. Uncertain_for_abstract_screening
   - 제목만으로는 판단이 어렵지만 관련 가능성이 있어 abstract 확인이 필요함

3. Exclude
   - 제목만으로 연구질문과 명백히 무관하거나 제외 기준에 해당함

4. Snowball_only
   - review, systematic review, meta-analysis 등으로 최종 분석에는 제외하지만 참고문헌 추적에 활용 가능함

5. Article_type_check_needed
   - letter, reply, commentary, editorial 등 article type 확인이 필요한 경우

Corrected_Reason_Code는 아래 중 하나만 사용한다:
- likely_relevant_hp_colorectal_polyp
- relevant_hp_colorectal_adenoma
- relevant_hp_advanced_neoplasia
- relevant_hp_serrated_polyp
- gastric_pathology_colorectal_outcome
- colorectal_neoplasia_uncertain
- crc_only_uncertain
- gastric_only_no_colorectal_outcome
- wrong_exposure
- wrong_outcome
- wrong_population
- review_or_meta
- letter_reply_commentary
- case_report
- animal_or_invitro
- mechanistic_only
- unrelated
- unclear_title_only

Correction_Type은 아래 중 하나만 사용한다:
- Keep_original
- Downgrade_include
- Rescue_exclude
- Recode_reason
- Keep_uncertain
- Keep_snowball
- Article_type_recheck

Corrected_Next_Action은 아래 중 하나만 사용한다:
- Retrieve abstract
- Exclude from further screening
- Use for citation chasing
- Check article type
- Human review needed

작업 절차:
1. title_screening_stage2_results_v2.csv를 읽는다.
2. stage2_title_screening_audit_flags.csv가 있으면 이를 우선 참고한다.
3. selected_papers.csv는 Include_fulltext 추출 결과로만 참고하고, 최종 후보군으로 간주하지 않는다.
4. 각 논문에 대해 Corrected_Decision, Corrected_Reason_Code, Correction_Type, Corrected_Next_Action을 부여한다.
5. 기존 Stage2_Decision과 Corrected_Decision이 달라진 경우 Reviewer_Comment에 변경 이유를 간단히 기록한다.
6. 판단 근거는 Title_Evidence에 제목에서 확인 가능한 문구로만 기록한다.
7. 전체 감사 결과 파일을 생성한다.
8. Corrected_Decision이 Include_for_abstract_screening 또는 Uncertain_for_abstract_screening 또는 Article_type_check_needed인 논문만 추출하여 abstract screening 후보 파일을 생성한다.
9. Snowball_only 논문은 별도 citation chasing 파일로 생성한다.
10. Exclude 논문은 별도 excluded 파일로 생성한다.

출력 파일:
1. stage2_title_screening_audit_corrected.csv
   - 전체 653개 논문에 대한 감사·보정 결과

2. abstract_screening_candidates_corrected.csv
   - 다음 abstract screening에 사용할 후보 논문
   - Include_for_abstract_screening, Uncertain_for_abstract_screening, Article_type_check_needed 포함

3. snowball_only_papers.csv
   - review/meta-analysis 등 참고문헌 추적용 논문

4. title_audit_excluded_papers.csv
   - title audit 후 제외된 논문

출력 컬럼:
stage2_title_screening_audit_corrected.csv에는 아래 컬럼을 포함한다.

ID,
Publication Year,
First Author,
Title,
Journal,
DOI_URL,
Original_Decision,
Original_Reason_Code,
Original_Confidence,
Corrected_Decision,
Corrected_Reason_Code,
Correction_Type,
Corrected_Next_Action,
Title_Evidence,
Reviewer_Comment,
Corrected_Confidence

abstract_screening_candidates_corrected.csv에는 아래 컬럼을 포함한다.

ID,
Publication Year,
First Author,
Title,
Journal,
DOI_URL,
Corrected_Decision,
Corrected_Reason_Code,
Corrected_Next_Action,
Title_Evidence,
Reviewer_Comment,
Corrected_Confidence

작업 완료 후 요약 보고:
작업이 끝나면 아래 내용을 간단히 보고하라.

1. 전체 논문 수
2. 기존 Stage2_Decision 분포
3. Corrected_Decision 분포
4. Include에서 Exclude 또는 Uncertain으로 내려간 논문 수
5. Exclude에서 abstract screening 후보로 rescue된 논문 수
6. Snowball_only 논문 수
7. 다음 단계에 사용할 파일명
8. 사람이 우선 확인해야 할 Critical 항목 목록

주의:
결과는 보수적으로 작성한다.
title-only 단계에서 애매한 논문은 버리지 않는다.
다음 단계의 목적은 full-text screening이 아니라 abstract screening이다.
```

<a id="d1-u14"></a>

## D1-U14

**Mapped outputs:** `05; 06; C1; C3`  
**Prompt type:** refinement  
**Source-reported status:** 수정에 사용 확인  
**SHA-256:** `885a85e75fad90ad26574329fa17abb0709e24edf59fa97bafd5e2a6e2d0855c`

```text
너는 에이전트 모드에서 실행되는 메타분석 abstract screening 후보군 정제자다.

목표:
abstract_screening_candidates_corrected.csv 파일을 검토하여,
title-only 기준에서 명백히 부적절한 후보를 제거하고,
실제 abstract screening에 투입할 최종 후보군 CSV를 생성한다.

입력 파일:
abstract_screening_candidates_corrected.csv

연구질문:
Helicobacter pylori infection 또는 H. pylori 관련 gastric pathology가
colorectal polyps, colonic polyps, colorectal adenoma, advanced adenoma,
advanced colorectal neoplasia, serrated polyp, colorectal neoplasia와
관련되는지 평가하는 인간 대상 원저 연구를 선별한다.

중요:
이 단계는 여전히 title-only refinement이다.
abstract나 full text 내용을 추정하지 않는다.
제목에서 확인 가능한 정보만 사용한다.

핵심 원칙:
1. “polyp”라는 단어만 보고 포함하지 않는다.
2. gastric polyp, gastric hyperplastic polyp, fundic gland polyp, gastric adenoma, gastric lesion만 있고 colorectal/colon/rectal outcome이 없으면 제외한다.
3. colorectal polyp, colonic polyp, colon polyp, colorectal adenoma, colonic adenoma, advanced adenoma, colorectal neoplasia, advanced colorectal neoplasia, serrated colonic polyp, sessile serrated polyp이 제목에 보이면 후보로 남긴다.
4. H. pylori, Helicobacter pylori, HP, CagA, VacA, eradication, atrophic gastritis, gastric atrophy, intestinal metaplasia, gastric histopathology, gastric mucosal atrophy가 exposure로 보이면 후보로 남긴다.
5. 제목에 colorectal cancer만 있고 polyp/adenoma/neoplasia 자료가 있는지 불분명하면 Low priority로 남긴다.
6. review, systematic review, meta-analysis, umbrella review는 abstract screening 후보가 아니라 Snowball_only로 분류한다.
7. letter, reply, commentary, editorial은 Article_type_check_needed로 분류한다.
8. case report는 제외한다.
9. animal, in vitro, cell-line, molecular mechanism-only, probiotic/compound 실험 연구는 제외한다.
10. 판단이 애매하면 제외하지 말고 Uncertain_for_abstract_screening으로 둔다.

Refined_Decision은 아래 중 하나만 사용한다:
- Include_for_abstract_screening
- Uncertain_for_abstract_screening
- Low_priority_abstract_screening
- Exclude_title_only
- Snowball_only
- Article_type_check_needed

Refined_Reason_Code는 아래 중 하나만 사용한다:
- direct_hp_colorectal_polyp
- direct_hp_colorectal_adenoma
- direct_hp_colorectal_neoplasia
- direct_hp_serrated_polyp
- gastric_pathology_colorectal_outcome
- crc_only_low_priority
- gastric_polyp_only
- gastric_cancer_only
- wrong_exposure
- wrong_outcome
- review_or_meta
- letter_reply_commentary
- case_report
- animal_or_invitro
- mechanistic_only
- unclear_title_only

작업 절차:
1. abstract_screening_candidates_corrected.csv를 읽는다.
2. 각 논문의 Title을 기준으로 다시 판정한다.
3. 기존 Corrected_Decision과 비교하여 변경 여부를 기록한다.
4. gastric polyp only 논문은 반드시 Exclude_title_only로 내린다.
5. H. pylori와 colorectal polyp/adenoma/neoplasia가 함께 보이는 논문은 Include_for_abstract_screening으로 유지한다.
6. colorectal cancer only 논문은 Low_priority_abstract_screening으로 둔다.
7. 결과 전체 파일을 저장한다.
8. Refined_Decision이 Include_for_abstract_screening, Uncertain_for_abstract_screening, Low_priority_abstract_screening인 논문만 추출하여 최종 abstract screening 입력 파일을 생성한다.
9. Snowball_only와 Article_type_check_needed는 별도 파일로 저장한다.
10. Exclude_title_only는 별도 파일로 저장한다.

출력 파일:
1. abstract_screening_candidates_refined_audit.csv
   - 207개 전체 후보군의 재검토 결과

2. abstract_screening_input_final.csv
   - 실제 abstract screening에 사용할 최종 후보군

3. abstract_screening_low_priority.csv
   - colorectal cancer only 등 우선순위 낮은 후보군

4. title_refinement_excluded.csv
   - title-only refinement에서 제외된 논문

5. snowball_or_article_type_check.csv
   - snowball only 또는 article type 확인 대상

출력 컬럼:
ID,
Publication Year,
First Author,
Title,
Journal,
DOI_URL,
Previous_Decision,
Previous_Reason_Code,
Refined_Decision,
Refined_Reason_Code,
Refinement_Type,
Refined_Next_Action,
Title_Evidence,
Reviewer_Comment,
Refined_Confidence

Refinement_Type은 아래 중 하나만 사용한다:
- Keep
- Downgrade_to_uncertain
- Downgrade_to_low_priority
- Exclude_gastric_only
- Exclude_wrong_topic
- Reclassify_snowball
- Reclassify_article_type
- Recode_reason

작업 완료 후 요약 보고:
1. 입력 후보 수
2. Refined_Decision 분포
3. 최종 abstract screening 입력 파일의 논문 수
4. 제외된 gastric polyp only 논문 수
5. Low priority 논문 수
6. Snowball/article type check 논문 수
7. 사람이 우선 확인해야 할 논문 ID 목록

주의:
이 단계의 목적은 full-text screening이 아니다.
최종 포함 여부를 결정하지 말고, abstract screening에 투입할 후보군을 정리하라.
```

<a id="d1-u15"></a>

## D1-U15

**Mapped outputs:** `07; 09; C1`  
**Prompt type:** 최초 실행  
**Source-reported status:** 직접 사용 확인  
**SHA-256:** `acfa023678a73f3c7fffdea1626f4b95a56dfe48ae6288c1aa776b9d615e418f`

```text


너는 에이전트 모드에서 실행되는 메타분석 title/abstract screening reviewer다.

목표:
abstract_screening_input_final_manual_patch.csv 파일에 포함된 논문들의 abstract를 확인하여,
full-text screening으로 넘길 논문을 선별한다.

입력 파일:
abstract_screening_input_final_manual_patch.csv

연구질문:
Helicobacter pylori infection 또는 H. pylori 관련 gastric pathology가
colorectal polyps, colonic polyps, colorectal adenoma, advanced adenoma,
advanced colorectal neoplasia, serrated polyp, colorectal neoplasia와
관련되는지 평가하는 인간 대상 원저 연구를 선별한다.

중요:
이 단계는 title/abstract screening이다.
최종 메타분석 포함 여부를 확정하는 단계가 아니다.
목표는 full-text screening 후보를 선별하는 것이다.
애매하면 제외하지 말고 full-text 확인 후보로 남긴다.

작업 절차:
1. 입력 파일을 읽는다.
2. DOI_URL 또는 PubMed 정보를 이용해 가능한 경우 PMID, article type, abstract를 보강한다.
3. abstract를 찾을 수 없는 경우 Abstract_Status를 Not_found로 표시하고, 제목 기준으로 보수적으로 판단한다.
4. 각 논문에 대해 title과 abstract를 함께 검토한다.
5. full-text screening으로 넘길지 여부를 판정한다.
6. 결과 CSV 파일을 생성한다.
7. full-text screening 후보만 별도 CSV로 생성한다.
8. 제외 논문은 제외 사유와 함께 별도 CSV로 생성한다.
9. Snowball 또는 article type 확인 대상도 별도 CSV로 생성한다.

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
1. stage2_title_abstract_screening_results.csv
   - 전체 입력 논문에 대한 title/abstract screening 결과

2. fulltext_screening_candidates.csv
   - Include_for_fulltext, Uncertain_retrieve_fulltext 논문만 포함

3. stage2_abstract_excluded.csv
   - Exclude 논문과 제외 사유

4. stage2_snowball_article_check.csv
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
2. abstract를 찾은 논문 수
3. abstract를 찾지 못한 논문 수
4. Stage2_Abstract_Decision 분포
5. full-text screening 후보 수
6. 제외 논문 수와 주요 제외 사유
7. Snowball/article type check 논문 수
8. 사람이 우선 확인해야 할 논문 ID 목록

주의:
이 단계에서 최종 포함 여부를 확정하지 않는다.
애매한 논문은 full text 확인 후보로 남긴다.
colorectal cancer only 논문은 abstract에서 polyp/adenoma/neoplasia 자료가 확인되지 않으면 제외한다.
gastric polyp only 논문은 colorectal outcome이 없으면 제외한다.
```
