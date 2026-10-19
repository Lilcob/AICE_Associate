# 그림 재현 안내

## 회귀 신경망의 로그와 학습 곡선

회귀 프로젝트 13·14번 문항의 그림은 **별도 합성 데이터 40행**으로 만든 문법 시연입니다. 원래 부동산 관측자료의 결과가 아닙니다. 입력 생성·전처리·학습을 한 번에 실행하려면 다음 명령을 사용합니다.

```bash
python -m pip install -r scripts/regression_example/requirements.txt
python scripts/regression_example/run_all.py
```

Python 3.12의 CPU 환경에서 확인했습니다. 패키지 버전·운영체제·장치가 바뀌면 같은 시드여도 결과가 달라질 수 있습니다. 실행하면 해당 폴더 안의 `data/`와 `run/`에 동명 재현 파일을 생성합니다.

1. `generate_synthetic_data.py`는 시드 2027로 가상 주택 40행과 지역 정보를 만듭니다.
2. `reproduce_curve.py`는 분할 시드 42로 훈련 32행·검증 8행을 준비하고, 훈련 자료에서만 인코딩 열과 표준화 기준을 만듭니다.
3. 모델 시드 1로 원고와 같은 신경망을 50에포크, 배치 크기 32로 학습합니다. 한 실행의 history에서 CSV·로그·그림을 함께 저장하며 반복 실행도 비교합니다.

본문에서 설명을 줄였지만 입력 준비가 생략된 것은 아닙니다. [`step13_input.py`](../scripts/regression_example/step13_input.py)와 [`manuscript_model_exact.py`](../scripts/regression_example/manuscript_model_exact.py)를 같은 폴더에서 순서대로 읽으면 입력 배열과 모델의 연결을 확인할 수 있습니다.

[저장된 학습 기록](../assets/reproduced/history.csv), [로그 발췌](../assets/reproduced/training_log_excerpt.txt), [그림](../assets/reproduced/regression_learning_curve.png)은 같은 실행에서 생성했습니다. 기록의 마지막 훈련 MSE는 1888.9155, 검증 MSE는 3052.5781입니다. 원래 프로젝트의 다른 모델 성능과 직접 비교하지 않습니다.

## 추가 개념도

[개념 노트북](../notebooks/2027_concepts.ipynb)은 데이터 파일 없이 작은 계산을 실행합니다. [원본 이미지 폴더](../assets/concepts)의 PNG는 300dpi이며 SVG와 PDF도 함께 제공합니다.

```bash
python scripts/render_concepts.py
```

그림 생성기는 한글 글꼴로 AppleGothic을 사용합니다. 다른 운영체제에서는 스크립트의 글꼴 경로를 설치된 한글 글꼴로 지정하세요. 브로드캐스팅·병합·인코딩 값은 실제 라이브러리 연산으로 확인했으며, 학습 곡선 그림은 경향을 설명하는 개념도라고 표시했습니다.
