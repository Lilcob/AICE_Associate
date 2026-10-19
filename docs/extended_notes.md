# 추가 설명과 확장 실습

본문에서는 핵심 개념과 결과 해석을 확인하고, 자세한 중간 출력과 실험은 여기서 이어갑니다.

<a id="method-chaining"></a>
## 메서드 체이닝의 중간 결과

새 표를 반환하는 메서드는 이어서 호출할 수 있습니다. 원본을 수정하고 `None`을 반환하는 `insert()`는 체이닝이 끝난 뒤 호출합니다.

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
step1 = df.assign(C=df['A'] + df['B'])
step2 = step1.replace({'B': {5: 50}})
step3 = step2.assign(A=lambda frame: frame['A'] * 2)
step3.insert(1, 'D', [100, 200, 300])
print(step1)
print(step2)
print(step3)
```

최종 열 순서는 A·D·B·C입니다. `C`는 첫 단계의 A+B로 계산했으므로 이후 A를 두 배로 바꿔도 자동으로 다시 계산되지 않습니다. 최종 세 행은 다음과 같습니다.

```text
   A    D   B  C
0  2  100   4  5
1  4  200  50  7
2  6  300   6  9
```

`df_alias = df`는 같은 객체에 다른 이름을 붙입니다. `copy()`는 별도 객체를 만들지만, object 열 안의 중첩 Python 객체까지 재귀적으로 복사하지는 않습니다. `copy(deep=False)`의 수정 전파는 pandas의 Copy-on-Write 설정에도 영향을 받습니다. pandas 3.0에서는 Copy-on-Write가 기본이며, 본문의 버전 고정 실습과 구분해 확인합니다. [pandas Copy-on-Write 안내](https://pandas.pydata.org/docs/user_guide/copy_on_write.html)

<a id="category-benchmark"></a>
## category의 메모리와 실행 시간

반복 범주를 코드와 범주 목록으로 저장하면 메모리를 줄일 수 있습니다. 고유값이 많거나 문자열 저장 방식이 다르면 효과도 달라집니다. 변환 비용과 그룹화 시간을 따로 측정하며, category가 언제나 더 빠르다고 가정하지 않습니다.

```bash
python scripts/category_benchmark.py --rows 200000 --repeat 3
```

본문에서 옮긴 대규모 실험은 `--rows 2000000`으로 실행합니다. 결과에는 원본·category 메모리, 복사·변환 시간, 두 종류 키의 그룹화 시간이 표시됩니다. 같은 그룹과 평균을 계산했는지도 코드에서 확인합니다. 시간은 실행 환경마다 달라지므로 특정 초 단위를 정답처럼 비교하지 않습니다.

[실험 코드](../scripts/category_benchmark.py)는 `observed=True`를 명시해 관측된 범주 조합만 집계합니다. 데이터 행 수, 고유 범주 수, pandas 버전과 반복 측정값을 함께 보세요.

<a id="sample-statistics"></a>
## 표본 표준편차와 분산 계산

본문의 허리둘레 예시 `[80.0, 90.0, 96.0, 85.0, 84.5]`는 평균 87.1, 중앙값 85.0입니다. 기본 `std()`는 편차 제곱합을 n-1로 나눈 뒤 제곱근을 계산합니다. 결과는 약 6.11입니다.

```python
import pandas as pd
waist = pd.Series([80.0, 90.0, 96.0, 85.0, 84.5])
weight = pd.Series([70, 55, 65, 70, 65])
print(waist.mean(), waist.median(), waist.std(ddof=1))
print(weight.var(ddof=1))  # 37.5
print(waist.std(ddof=0))  # 모집단 기준은 분모가 n
```

NumPy의 `np.std()` 기본값은 `ddof=0`입니다. pandas의 기본값 `ddof=1`과 맞추지 않으면 같은 값에서도 결과가 다릅니다. 표본이 하나뿐인 그룹의 `std(ddof=1)`는 NaN입니다. 평균과 중앙값이 다르다는 이유만으로 작은 표본의 분포 형태를 확정하지 않습니다.

## 자료형과 버전 차이

`astype()`는 지정한 자료형으로 변환하며, `to_numeric(errors='coerce')`는 숫자로 바꾸지 못한 문자열을 NaN으로 처리합니다. `infer_objects()`는 이미 들어 있는 Python 값의 자료형을 추론하며 숫자·날짜 문자열을 자동으로 파싱하는 함수는 아닙니다.

pandas 2.x와 3.0에서는 문자열과 날짜·시간의 기본 추론이 달라질 수 있습니다. 예를 들어 날짜 변환 결과가 `datetime64[ns]` 또는 `datetime64[us]`로 표시될 수 있으므로 `dtype`을 직접 확인하세요. [pandas 자료형 안내](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)

## 여섯 가지 개념의 작은 실행 예시

[개념 노트북](https://colab.research.google.com/github/Lilcob/AICE_Associate/blob/main/notebooks/2027_concepts.ipynb)에서 브로드캐스팅, loc·iloc, 병합, 원핫 인코딩, 손실 계산, 검증 손실의 최저점을 확인합니다. 실제 고객이나 모델 성능을 보고하는 자료가 아닙니다.

- 브로드캐스팅: 오른쪽 차원부터 같은 크기 또는 1인지 확인합니다. [NumPy 공식 설명](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- loc·iloc: 레이블 슬라이스는 끝을 포함하고 정수 위치 슬라이스는 끝을 제외합니다. [pandas 공식 설명](https://pandas.pydata.org/docs/user_guide/indexing.html)
- merge: 중복 키는 결과 행 수를 늘릴 수 있습니다. pandas에서는 양쪽 결측 키끼리도 연결될 수 있어 SQL과 구분해야 합니다. [merge API](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)
- 원핫 인코딩: 훈련에서 fit한 범주와 열 순서를 검증에서도 유지합니다. [OneHotEncoder API](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
- 출력층과 손실: 확률 출력은 `from_logits=False`에 맞춰 사용합니다. [Keras 손실함수](https://keras.io/api/losses/probabilistic_losses/)
- 조기 종료: 감시 지표·방향·patience·min_delta와 가중치 복원을 구분합니다. [EarlyStopping API](https://keras.io/api/callbacks/early_stopping/)
