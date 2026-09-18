# Context Orchestration SR/MA — Prompt Archive

Prompt-provenance materials accompanying **“Context Orchestration for Managing Uncertainty in Large Language Model-Assisted Systematic Reviews and Meta-Analyses: Proof-of-Concept Study.”**

[한국어 안내](README_KO.md)

> Recovered user-request text is mapped to manuscript-reported outputs. Missing prompts are not reconstructed. Post-hoc numerical verification is kept separate from historical execution evidence.

## Start here

| Purpose | Open |
|---|---|
| Find the prompt for a manuscript output | [Outputs 01–32](outputs/README.md) |
| Browse every preserved request | [Conversation 1](prompts/D1.md) · [Conversation 2](prompts/D2.md) · [Conversation 3](prompts/D3.md) |
| Filter all 55 requests and inspect original checksums | [Prompt index](prompt_index.csv) |
| Inspect core, supporting and other recorded requests | [Output mapping and limits](output_prompt_map.csv) |
| Review incomplete evidence | [Recovery gaps](audit/RECOVERY_GAPS.md) |
| Understand the data stages | [Dataset lineage](evidence/DATASET_LINEAGE.md) |
| Read the scope of the earlier numerical check | [Numerical replay](evidence/NUMERIC_REPLAY.md) |
| Review the repository check | [Pre-publication check](audit/PRE_PUBLICATION_CHECK.md) |

## How to read a prompt

Click a prompt ID in the output index. Each prompt section contains the recovered request text, mapped output IDs, prompt type, source-reported use status, and the original text's SHA-256.

`D1-U01`, `D2-P09` and `D3-U05` are archive-local labels, not original platform message IDs or authenticated timestamps. Repeated submissions and correction requests remain separate occurrences. Source-reported execution does not by itself establish successful execution or manuscript adoption.

## Coverage labels

| Label | Meaning |
|---|---|
| 대응 원문 확인 | A recovered request directly corresponds to the reported task/output. |
| 부분 대응·근거 부족 | Related text exists, but the complete output chain is not fully supported. |
| 기준 차이·버전 확인 | Stage definitions, counts or versions differ and are recorded as such. |
| 원문 미확인 | The execution request was not recovered from the three available conversation extracts. |

A missing prompt is not evidence that a task was performed manually. The prompts for output categories 26–30 and 32 remain unrecovered.

## Dataset-stage distinction

The available artifacts document a **38-study pooling/QA set**, a **later 37-study analysis-preparation file** after removal of Study_ID 268, and an **unchanged 34-study H. pylori infection primary subset**. The adjusted-effects analysis has 26 studies; the later 24-study adjusted-OR-only analysis is a separate operation. See [dataset lineage](evidence/DATASET_LINEAGE.md).

## Text verification

All 55 prompt occurrences are present. The recorded checksums refer to the original extracted text, not the entire Markdown file. Three displayed code blocks omit one terminal newline; they are labelled in `prompt_index.csv`. No wording difference was detected.

```bash
python validation/verify_published_prompts.py
```

This checks archive consistency, not original platform logs or scientific validity.

## Publication and reuse

Repository visibility is controlled separately in GitHub Settings. The pre-publication check did not change it. Commit metadata can expose the account's author email; details and review limits are in the [check report](audit/PRE_PUBLICATION_CHECK.md).

No reuse licence has been assigned. Unrecovered prompts and unresolved evidence gaps are disclosed rather than filled in or treated as completed work.
