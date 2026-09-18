# Pre-publication repository check

## Scope

The initial live default-branch snapshot was commit `ff27934d1ee559bd0345b6ad9385e1e83a06c90e` (17 files). The check compared the uploaded prompt text with the supplied v1.0 prompt archive, inspected navigation and documentation, scanned the current prompt files for common secret/private-link patterns, and checked Actions-run and latest-commit metadata. Existing research results were not recalculated or amended.

## Results

| Check | Result |
|---|---|
| Preserved prompt occurrences | All 55 unique archive IDs are present: D1 29, D2 14, D3 12. No prompt wording is missing or altered relative to the supplied archive. |
| Exact text boundaries | 52 extracted code-block bodies match exactly. D1-U04, D1-U23 and D1-U24 differ only by one omitted terminal LF at the Markdown fence boundary. These are explicitly marked `TERMINAL_NEWLINE_ONLY` in the index. |
| Prompt checksums | The recorded SHA-256 values refer to the original extracted prompt text, not the surrounding Markdown. The validator accepts the documented one-terminal-LF difference and no other normalization. |
| Navigation | The output index linked to an absent `output_prompt_map.csv`. The missing compact mapping has been added, along with a 55-row `prompt_index.csv` pointing to actual uploaded files and anchors. |
| Current sensitive content | No API keys, private keys, credential-like tokens, private Drive document links, signed download links or personal absolute file paths were detected in the inspected prompt files. No manuscript document, source workbook or private-evidence ZIP is in the inspected default-branch tree. Documentation was also inspected. This is a bounded check, not a guarantee that every historical object is free of sensitive information. |
| Commit privacy | The inspected commit author/committer metadata contains the account's Gmail address. That metadata is separate from file contents and can be visible after publication. The address and commit history were not rewritten. |
| Actions | The live Actions API returned zero workflow runs at the time of inspection. |
| Research limitations | The six unrecovered execution-prompt categories and other evidence gaps remain explicitly documented; no missing prompt was invented or reclassified as manual work. |
| Dataset scope | The 38-study QA set, later 37-study preparation file, 34-study primary subset, and 26-study adjusted-effects analysis remain distinct. |
| Visibility | No visibility change was performed. The connected GitHub action set exposes file operations but no repository-visibility update action. |

## Re-run the text check

From a local copy of this repository with Python 3.9 or later:

```bash
python validation/verify_published_prompts.py
```

Expected result: 55 prompt occurrences, 32 output mappings and three documented terminal-LF display notes, with no content mismatch. The script checks the published representation against the recorded hashes; it does not authenticate the original ChatGPT logs.

## Boundaries of this review

This check did not audit all historical Git objects, other branches, tags, issues or pull requests. It did not decide the acceptability of publishing the commit-author email, assign a reuse licence, certify human adjudication, or resolve the manuscript/evidence gaps in [RECOVERY_GAPS.md](RECOVERY_GAPS.md). The repository owner controls the final visibility setting.

See [prompt index](../prompt_index.csv), [output mapping](../output_prompt_map.csv), [dataset lineage](../evidence/DATASET_LINEAGE.md) and [numerical verification scope](../evidence/NUMERIC_REPLAY.md).
