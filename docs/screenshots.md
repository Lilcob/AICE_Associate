# 화면을 보면서 따라해보기

제1장의 노트북 화면은 JupyterLab에서 예제 코드를 실제로 실행해 캡처했습니다. 아래 노트북을 열면 같은 코드와 실행 결과를 살펴볼 수 있습니다. 실제 AICE 시험 화면을 캡처한 자료는 아닙니다. 책에 넣은 화면은 글씨를 읽기 쉽도록 원본 캡처의 여백만 잘랐으며, 코드나 결과를 덧그리지 않았습니다. [인쇄용 캡처](../assets/screenshots/print)와 원본을 함께 볼 수 있습니다.

| 내용 | 노트북 | 캡처 |
|---|---|---|
| 데이터 불러오기와 기본 정보 확인 | [01_data_loading.ipynb](../notebooks/screens/01_data_loading.ipynb) | [화면](../assets/screenshots/01_data_loading.jpg) |
| 결측값 처리와 조건에 맞는 행 선택 | [02_preprocessing.ipynb](../notebooks/screens/02_preprocessing.ipynb) | [화면](../assets/screenshots/02_preprocessing.jpg) |
| 선 그래프와 제목 축 이름 지정 | [03_visualization.ipynb](../notebooks/screens/03_visualization.ipynb) | [화면](../assets/screenshots/03_visualization.jpg) |
| 그룹별 평균 계산하기 | [04_groupby.ipynb](../notebooks/screens/04_groupby.ipynb) | [화면](../assets/screenshots/04_groupby.jpg) |
| 데이터를 나누고 모델 학습하기 | [05_machine_learning.ipynb](../notebooks/screens/05_machine_learning.ipynb) | [화면](../assets/screenshots/05_machine_learning.jpg) |
| 혼동 행렬과 분류 평가 지표 | [06_evaluation.ipynb](../notebooks/screens/06_evaluation.ipynb) | [화면](../assets/screenshots/06_evaluation.jpg) |
| 신경망의 출력층과 학습 설정 | [07_deep_learning.ipynb](../notebooks/screens/07_deep_learning.ipynb) | [화면](../assets/screenshots/07_deep_learning.jpg) |
| 학습 기록으로 훈련 검증 곡선 그리기 | [08_history.ipynb](../notebooks/screens/08_history.ipynb) | [화면](../assets/screenshots/08_history.jpg) |

데이터 불러오기 예제의 [data.csv](../notebooks/screens/data.csv)는 이름·나이·매출을 넣은 작은 학습용 파일입니다. `01_data_loading.ipynb`와 같은 폴더에 두고 실행하세요. Colab에서 실행한다면 파일을 먼저 업로드해주세요. 원래 책의 건강검진 원자료가 아닙니다.

학습 곡선 예제는 [history.csv](../notebooks/screens/history.csv)를 같은 폴더에 두고 실행합니다. 이 기록은 별도 합성 데이터 40행으로 회귀 신경망을 재현한 실행에서 얻었습니다. 원래 부동산 관측자료의 예측 성능과 비교하지 않습니다. 입력 생성부터 해보고 싶다면 [그림 재현 안내](reproduce_figures.md)를 참고하세요.

공식 출제범위 화면은 [AICE Associate 소개](https://aice.study/info/aice/asso)에서 2026년 10월 19일에 캡처했습니다. 시험 조건은 바뀔 수 있으므로 응시할 회차의 안내도 함께 확인해주세요.
