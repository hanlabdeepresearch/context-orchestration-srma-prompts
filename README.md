# Context Orchestration SR/MA — Prompt Archive

Private review repository for the prompt provenance package accompanying **“Context Orchestration for Managing Uncertainty in Large Language Model-Assisted Systematic Reviews and Meta-Analyses: Proof-of-Concept Study.”**

> This repository preserves recovered user-request text and maps it to manuscript-reported outputs. Missing prompts are not reconstructed, and post-hoc numerical verification is kept separate from historical execution evidence.

## Start here

1. **[Manuscript output index](outputs/README.md)** — outputs 01–32 with coverage status and direct links to the recovered core prompt(s).
2. **[Conversation 1 prompts](prompts/D1.md)** · **[Conversation 2 prompts](prompts/D2.md)** · **[Conversation 3 prompts](prompts/D3.md)** — preserved request text organized by archival prompt ID.
3. **[Recovery gaps](audit/RECOVERY_GAPS.md)** — outputs or workflow steps whose original execution prompt/evidence is incomplete.
4. **[Dataset lineage](evidence/DATASET_LINEAGE.md)** — 42-study extraction → 38-study pooling/QA → later 37-study analysis-preparation file → unchanged 34-study primary subset.
5. **[Numerical verification](evidence/NUMERIC_REPLAY.md)** — scope and limits of the post-hoc numerical replay.

## How to review a prompt

From the [output index](outputs/README.md), click a prompt ID such as `D1-U14`, `D2-P09`, or `D3-U05`. The prompt page shows:

- the preserved user-request text;
- the manuscript output(s) mapped to that request;
- prompt type (initial run, refinement, QA, rerun, etc.);
- source-reported use status; and
- SHA-256 recorded in the extraction archive.

The prompt IDs are **archive-local identifiers**, not original platform message IDs or authenticated timestamps. Repeated submissions and correction prompts are retained as separate occurrences.

## Coverage status

The output index uses four labels:

- `대응 원문 확인` — a recovered request directly corresponds to the reported task/output;
- `부분 대응·근거 부족` — related prompt text exists, but the complete output chain is not fully supported;
- `기준 차이·버전 확인` — prompt/output records exist but stage definitions or versions differ and are preserved as such;
- `원문 미확인` — the execution prompt was not recovered from the available three conversation extracts.

A missing prompt is **not** evidence that a task was performed manually.

## Important dataset-stage note

The available artifacts document a **38-study pooling/QA set**, a **later 37-study analysis-preparation file** after removal of Study_ID 268, and an **unchanged 34-study H. pylori infection primary subset**. These stages are kept distinct rather than silently reconciled. See [DATASET_LINEAGE.md](evidence/DATASET_LINEAGE.md).

## Repository layout

```text
README.md
outputs/README.md       # output 01–32 → prompt navigation
prompts/                # recovered prompt text, organized by conversation
reviewer/               # compact reviewer-facing mapping table
evidence/               # dataset lineage and numerical replay notes
audit/                  # recovery gaps and limitations
```

## Publication status

This repository is currently **private for author review**. No licence has been assigned. Public release should occur only after author review of the prompt mappings, recovery gaps, and dataset-stage wording.
