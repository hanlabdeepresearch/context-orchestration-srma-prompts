# Context Orchestration SR/MA 프롬프트 아카이브

논문 **“Context Orchestration for Managing Uncertainty in Large Language Model-Assisted Systematic Reviews and Meta-Analyses: Proof-of-Concept Study”**의 실제 사용자 요청과 논문 산출물의 대응관계를 정리한 자료입니다.

## 확인 순서

| 확인할 내용 | 열기 |
|---|---|
| 논문 산출물별 사용 프롬프트 | [01–32 산출물 인덱스](outputs/README.md) |
| 대화별 원문 | [대화 1](prompts/D1.md) · [대화 2](prompts/D2.md) · [대화 3](prompts/D3.md) |
| 전체 55건의 위치·유형·체크섬 | [프롬프트 인덱스 CSV](prompt_index.csv) |
| 핵심·보조·다른 버전과 남은 확인사항 | [산출물 대응 CSV](output_prompt_map.csv) |
| 원문 미확인·근거 부족 사항 | [기록의 공백과 한계](audit/RECOVERY_GAPS.md) |
| 38편·37편·34편·26편의 관계 | [데이터셋 단계 설명](evidence/DATASET_LINEAGE.md) |
| 기존 수치 재현 검증의 범위 | [수치 검증 설명](evidence/NUMERIC_REPLAY.md) |
| 저장소 공개 전 점검 결과 | [공개 전 점검 보고서](audit/PRE_PUBLICATION_CHECK.md) |

## 원문 보존과 검증

보존한 요청은 55건이며, 반복 제출과 수정·재실행도 각각 유지했습니다. 게시된 프롬프트 55건의 문구를 보관본과 대조했습니다. 52건은 정확히 일치하고, D1-U04·D1-U23·D1-U24는 코드블록 경계에서 마지막 줄바꿈 한 개만 차이가 있습니다. CSV에 이를 표시했으며 문구는 변경하지 않았습니다.

체크섬은 Markdown 파일 전체가 아니라 보관된 원래 프롬프트 텍스트를 대상으로 합니다. 아래 검증 스크립트는 표시상 줄바꿈 차이를 명시적으로 구분합니다.

```bash
python validation/verify_published_prompts.py
```

`D1-U01` 등의 식별자는 아카이브용이며 원시 플랫폼 메시지 ID나 실행 시각이 아닙니다. 원문이 있다는 사실을 실행 성공·논문 채택·사람 검토 완료와 동일시하지 않습니다.

## 연구 기록상의 구분

38편 pooling/QA 자료, ID 268 제외 후의 37편 분석 준비 파일, 변화가 없는 34편 주 분석과 26편 보정 효과크기 분석을 구분합니다. 24편 adjusted-OR-only는 별도의 후속 작업입니다.

26–30번과 32번의 실제 실행 원문은 미확인 상태로 유지합니다. 없는 프롬프트를 새로 만들거나 연구자가 직접 수행했다고 추정하지 않습니다. 사후 수치 검증은 당시 실행 기록과 구분합니다.

## 공개 상태와 주의사항

저장소 공개 범위는 GitHub Settings에서 별도로 관리됩니다. 이번 점검에서는 공개 상태를 바꾸지 않았습니다. 기존 커밋에는 계정의 Gmail 주소가 작성자 정보로 기록되어 있으며 공개 시 함께 보일 수 있습니다. 과거 전체 Git 기록의 민감정보 검사를 완료한 것은 아닙니다.

미공개 원고 파일·원본 연구용 워크북·개인 Drive 증빙 묶음은 현재 게시 파일에 포함하지 않았습니다. 별도 재사용 License는 아직 부여하지 않았습니다.
