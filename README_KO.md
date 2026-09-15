# Context Orchestration SR/MA 프롬프트 아카이브

이 저장소는 논문 **“Context Orchestration for Managing Uncertainty in Large Language Model-Assisted Systematic Reviews and Meta-Analyses: Proof-of-Concept Study”**의 프롬프트 출처와 산출물 대응관계를 저자 검토용으로 정리한 **Private 저장소**입니다.

## 확인 순서

1. [논문 산출물 01–32 인덱스](outputs/README.md)에서 확인하려는 산출물을 찾습니다.
2. 연결된 `D1-Uxx`, `D2-Pxx`, `D3-Uxx` 프롬프트 ID를 클릭하면 실제 보존된 사용자 요청 원문으로 이동합니다.
3. [미확인·추가 확인사항](audit/RECOVERY_GAPS.md)에서 원문 미확보 또는 버전 차이를 확인합니다.
4. [데이터셋 단계 설명](evidence/DATASET_LINEAGE.md)에서 42편 추출 → 38편 pooling/QA → 37편 분석 준비 → 34편 주 분석의 관계를 확인합니다.
5. [수치 재현 검증 범위](evidence/NUMERIC_REPLAY.md)에서 논문 결과 수치와 사후 검증의 범위를 확인합니다.

## 프롬프트 기록 원칙

- 보관된 사용자 요청 원문은 새로 작성하거나 미화하지 않습니다.
- 반복 제출, 오류 수정, QA, 재실행 프롬프트는 별도의 기록으로 유지합니다.
- 프롬프트가 발견되지 않았다고 해서 연구자가 직접 수행했다고 추정하지 않습니다.
- 사후 수치 검증은 당시 실행 기록과 구분합니다.
- `D1-U01` 등의 ID는 아카이브용 식별자이며 플랫폼의 실제 메시지 ID나 인증된 시각이 아닙니다.

## 중요 데이터 단계

자료에는 **38편 pooling/QA 데이터셋**, 이후 Study_ID 268을 제외한 **37편 분석 준비 파일**, 그리고 그 변화에 영향을 받지 않는 **34편 H. pylori infection 주 분석 집합**이 모두 존재합니다. 이 단계들은 하나로 합치거나 임의로 수정하지 않고 구분하여 보존합니다.

## 공개 상태

현재 저장소는 **저자 확인을 위한 Private 상태**입니다. 저자 검토가 끝난 뒤에만 Public 전환을 권장합니다. 아직 별도 License는 부여하지 않았습니다.
