# Numerical replay: what was checked

The v0.3 audit applied three saved numerical functions from `generate_meta_analysis_plots.py` to the supplied analysis-preparation data. The existing REML, subgroup and adjusted-effects conditions were retained. Original research inputs were not modified.

The verification compared **30 manuscript-reported values** with replay values. All 30 agree at the specified reporting precision. This covers study counts, pooled odds ratios and confidence limits, I², primary Q and tau², and the reported Egger/Begg results.

| Analysis | k | Pooled OR | 95% CI | I² (%) |
|---|---:|---:|---|---:|
| Primary Hp infection | 34 | 1.73 | 1.49–2.02 | 88.0 |
| Adjusted effects | 26 | 1.71 | 1.42–2.07 | 90.2 |
| Colorectal adenoma | 28 | 1.69 | 1.44–1.98 | 81.9 |
| Any colorectal neoplasia | 4 | 1.50 | 1.07–2.09 | 96.5 |
| Advanced colorectal neoplasia | 2 | 3.76 | 0.65–21.65 | 94.1 |

Primary Egger intercept/P: 2.53 / 0.0002 at manuscript precision. Begg P: 3.9×10^-7 at manuscript precision.

## Limits

These are **post-hoc verification outputs**, not recovered historical `meta_analysis_results.xlsx` or a reconstruction of that missing file. The original results workbooks were not located in the searched Drive file names and relevant folders. Absence from that search is not a claim of absence from all storage.

The replay checks consistency with the saved implementation. It does not independently validate the statistical methodology, full-text extraction, cohort independence, or the original platform execution. The stored implementation can return 0 for very small Q-test p-values because it uses `1-cdf`; that is not reported here as an exact probability of zero.

The later 24-study adjusted-OR-only output is a different analysis, not a replacement for the manuscript's 26-study adjusted-effects analysis. The downloaded `Table_corrected.xlsx` is a screening-performance table with different denominators, not the meta-analysis result table.

The original code, source workbooks and replay helper scripts remain in the author's private evidence bundle.
