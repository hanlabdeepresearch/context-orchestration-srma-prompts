# Context Orchestration SR/MA — Prompt Archive

Private review repository for the prompt provenance package accompanying **“Context Orchestration for Managing Uncertainty in Large Language Model-Assisted Systematic Reviews and Meta-Analyses: Proof-of-Concept Study.”**

> This repository preserves recovered user-request text and maps it to manuscript-reported outputs. It does **not** reconstruct missing prompts, and it does not treat post-hoc verification as historical execution evidence.

## Quick review

- **[Reviewer prompt supplement](reviewer/PROMPT_SUPPLEMENT.md)** — all 55 preserved request occurrences in one document.
- **[Two-column reviewer table](reviewer/OUTPUT_PROMPT_TABLE.md)** — output-to-prompt summary.
- **[Conversation 1 prompts](prompts/D1.md)** · **[Conversation 2 prompts](prompts/D2.md)** · **[Conversation 3 prompts](prompts/D3.md)** — each prompt is directly addressable by ID.
- **[Prompt index](prompt_index.csv)** — machine-readable prompt metadata.
- **[Recovery gaps](audit/RECOVERY_GAPS.md)** — items whose original execution prompts were not recovered.
- **[Dataset lineage](evidence/DATASET_LINEAGE.md)** — 38-study QA set → later 37-study preparation file → unchanged 34-study primary subset.
- **[Numerical verification](evidence/NUMERIC_REPLAY.md)** — post-hoc verification scope and limits.

## Manuscript output index

Each output page lists the manuscript location, recovered core prompt(s), supporting/QA prompt(s), file evidence, and remaining limitations.

| ID | Output | Coverage | Page |
|---:|---|---|---|
| 01 | PECO 구조화 표 및 PubMed 검색식 | 대응 원문 확인 | [open](outputs/01.md) |
| 02 | 독립적 PubMed 검색 결과 보고 | 대응 원문 확인 | [open](outputs/02.md) |
| 03 | 전체 검색 문헌 데이터베이스 / 서지정보 CSV | 대응 원문 확인 | [open](outputs/03.md) |
| 04 | 1차 제목 선별 결과 CSV | 기준 차이·버전 확인 | [open](outputs/04.md) |
| 05 | 제목 선별 재검토·정제 결과 CSV | 대응 원문 확인 | [open](outputs/05.md) |
| 06 | 제목 판정 변경 이력 및 초록 선별 후보 파일 | 부분 대응·근거 부족 | [open](outputs/06.md) |
| 07 | 2차 초록 선별 결과 CSV | 기준 차이·버전 확인 | [open](outputs/07.md) |
| 08 | 누락 PMID·초록 보완 결과 및 배치별 갱신 파일 | 기준 차이·버전 확인 | [open](outputs/08.md) |
| 09 | 초록 보완 후 재선별 결과 및 전문 심사 후보 파일 | 기준 차이·버전 확인 | [open](outputs/09.md) |
| 10 | 3차 전문 적격성 심사 결과 및 근거 추출표 | 대응 원문 확인 | [open](outputs/10.md) |
| 11 | Awaiting information 문헌의 해결·최종 판정 결과 | 대응 원문 확인 | [open](outputs/11.md) |
| 12 | 전문 심사 제외·중복 코호트 문헌의 최종 QA 기록 | 대응 원문 확인 | [open](outputs/12.md) |
| 13 | 연구 특성 및 정량 데이터 추출표 | 부분 대응·근거 부족 | [open](outputs/13.md) |
| 14 | 대표 효과크기 선정 및 Log effect·SE 계산 데이터셋 | 대응 원문 확인 | [open](outputs/14.md) |
| 15 | 데이터 추출 배치별 완료 보고서 | 대응 원문 확인 | [open](outputs/15.md) |
| 16 | 노출·결과·효과크기 출처의 표준화 데이터셋 | 대응 원문 확인 | [open](outputs/16.md) |
| 17 | 분석 전 QA 이슈 파일 | 대응 원문 확인 | [open](outputs/17.md) |
| 18 | 중복 효과크기 의심 6편의 검토 반영 기록 | 부분 대응·근거 부족 | [open](outputs/18.md) |
| 19 | 최종 38편 메타분석 데이터셋 및 구성 분포표 | 대응 원문 확인 | [open](outputs/19.md) |
| 20 | 주 분석 결과 및 이질성·예측구간 출력 | 대응 원문 확인 | [open](outputs/20.md) |
| 21 | Outcome Group별 하위집단 분석 결과 | 대응 원문 확인 | [open](outputs/21.md) |
| 22 | Adjusted-only 민감도 분석 결과 | 대응 원문 확인 | [open](outputs/22.md) |
| 23 | Funnel plot 및 비대칭 관찰 결과 | 부분 대응·근거 부족 | [open](outputs/23.md) |
| 24 | Egger·Begg 검정 결과 | 대응 원문 확인 | [open](outputs/24.md) |
| 25 | 메타분석 결과표 및 참조 메타분석과의 비교 정리 | 부분 대응·근거 부족 | [open](outputs/25.md) |
| 26 | 참조 앵커 40편의 단계별 매칭·유지·소실 기록 | 원문 미확인 | [open](outputs/26.md) |
| 27 | ACR·단계별 유지율·FN·CRR 계산 결과 | 원문 미확인 | [open](outputs/27.md) |
| 28 | 비앵커 추가 후보 문헌 24편의 목록 및 적격성 검토 | 원문 미확인 | [open](outputs/28.md) |
| 29 | 양성 판정 범위를 달리한 성능 비교 결과 | 원문 미확인 | [open](outputs/29.md) |
| 30 | 초기 워크플로우와 개선 워크플로우의 성능 비교 근거 | 원문 미확인 | [open](outputs/30.md) |
| 31 | PRISMA 흐름도 및 단계별 문헌 수 집계 | 부분 대응·근거 부족 | [open](outputs/31.md) |
| 32 | Context Orchestration 7개 레이어 개념도 | 원문 미확인 | [open](outputs/32.md) |

## Reading the prompt records

Prompt IDs such as `D1-U01`, `D2-P09`, and `D3-U05` are **archive-local identifiers**. They are not original platform message IDs and do not imply authenticated timestamps. Repeated submissions and correction prompts are retained as separate occurrences.

Coverage labels distinguish direct correspondence, partial evidence, version/scope differences, and unrecovered prompt text. A missing prompt is not evidence that a task was performed manually.

## Important scope note

The available artifacts document a **38-study pooling/QA set**, a **later 37-study analysis-preparation file** after removing Study_ID 268, and an **unchanged 34-study H. pylori infection primary subset**. These stages are kept distinct rather than silently reconciled. See [DATASET_LINEAGE.md](evidence/DATASET_LINEAGE.md).

## Repository layout

```text
README.md
prompts/               # D1/D2/D3 prompt logs with direct anchors
outputs/               # 01–32 output-specific mapping pages
reviewer/              # reviewer-facing consolidated materials
common/                # C1–C3 cross-references; no invented master prompt
additional/            # NOS-related requests kept outside the 32 reported outputs
evidence/              # lineage and verification notes
audit/                 # recovery gaps
*.csv                  # machine-readable indexes
```

## Publication status

This repository is currently **private for author review**. No licence is assigned at this stage. Public release should occur only after author review of the scope notes, gaps, and manuscript-output mapping.
