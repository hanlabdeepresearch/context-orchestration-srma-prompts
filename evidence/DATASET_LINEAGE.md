# Dataset lineage and manuscript reporting scope

This note documents the available artifacts without rewriting the manuscript or the recovered instructions.

| Stage | Source artifact | Studies | Linked requests |
|---|---|---:|---|
| Full quantitative extraction set | Appendix 2, `Data extraction_42studies` | 42 | D2-P12; D2-P14 / D3-U01; D3-U02 |
| Records with `Included_for_Meta = Yes` | `meta_analysis_included_for_pooling.xlsx` | 38 | D3-U02 |
| Harmonized / pre-analysis QA set | `meta_analysis_dataset_QA.xlsx`; Appendix 2 `QA validation_38 studies` | 38 | D3-U03 |
| Subsequent analysis-preparation input | `meta_analysis_dataset_final.xlsx` | 37 | D3-U04 |
| Primary infection analysis | `Exposure_Group = Hp_infection` and `Included_for_Meta = Yes` | 34 | D3-U05 |
| Adjusted-effects sensitivity analysis | Primary set and `Effect_Source = Adjusted` | 26 | D3-U05 |
| Separate adjusted-OR-only analysis | Primary set and adjusted OR/OR effect type | 24 | D3-U12 → D3-U13 |

## File-level evidence

The QA workbook's full `A1:AK39` cell range matches the Appendix 2 QA sheet, including the header. The uploaded and Drive final workbooks were previously compared over `A1:V38` with identical cell values. Their research sets contain 38 and 37 records, respectively.

The sole removed Study_ID is **268 (Qing Y, 2016)**. In the QA file it is `Other_gastric_pathology`, `Secondary_Other`, and `Primary_Analysis_Eligible = No`. The excluded-final workbook contains that record. The reason “Not aligned with final exposure definition.” occurs in the D3-U04 instruction; it is not presented here as a separate adjudication note found in the excluded workbook.

For the 37 common records, all **740 values across 20 common columns** match. `Meta_Analysis_Group` is the remaining common column and its labels differ. The QA and final files have different full schemas; they are not byte-identical files.

The primary 34-study subset, effect values, confidence limits, log effects, standard errors, classifications, and 26-study adjusted-effects subset are unchanged by removal of Study_ID 268.

## A reporting distinction that remains important

The supplied manuscript describes all 38 studies as retained in the “final meta-analysis dataset.” The files separately document a 38-study QA set and a later 37-study analysis-preparation input. This archive preserves **both** facts; it does not silently reinterpret or amend that manuscript statement.

D3-U04 must not be labelled an unused experiment solely to make the prompt list match the number 38. It is an actual upstream instruction for the file named in D3-U05. Author-approved wording that distinguishes the stages is supplied separately in the working reviewer package, not inserted into the manuscript.

The unchanged primary subset explains why the 34-study numerical analysis can reproduce the manuscript despite the difference between the broader 38- and 37-study artifacts. It does not establish the accuracy of each full-text extraction, authenticate historical execution, or prove human review of the six duplicate-effect flags.
