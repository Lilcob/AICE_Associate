# 실습 시작하기

## 노트북 실행

저장소 첫 화면의 Colab 링크를 열어 본인 Drive에 사본을 저장한 뒤 위에서 아래로 실행합니다. NumPy와 개념 노트북은 외부 데이터 없이 시작할 수 있습니다.

pandas와 시각화 실습은 [원래 실습자료 폴더](https://drive.google.com/drive/folders/1h7zKKrHI6CH5IlrJh5uZ8OGfSmwd5scP)에서 건강검진 ZIP과 iris.zip을 내려받아 압축을 풉니다. `국민건강보험공단_건강검진정보_2023.CSV`와 `iris.data`를 노트북의 현재 폴더에 준비하세요. Colab에서는 왼쪽 파일 창에서 업로드할 수 있습니다.

```python
from pathlib import Path
print('현재 폴더:', Path.cwd())
print('건강 CSV:', Path('국민건강보험공단_건강검진정보_2023.CSV').is_file())
print('iris:', Path('iris.data').is_file())
```

건강 CSV는 cp949 인코딩으로 읽습니다. 파일이 크므로 업로드 후 준비가 끝났는지 확인합니다. 2023은 자료의 기준연도이고, 2027은 교재 개정판 연도입니다.

## 학습 환경

Python 3.12를 기준으로 확인한 패키지는 `requirements.txt`에 고정했습니다. 이는 실제 시험 서버의 설치 버전을 뜻하지 않습니다.

```bash
python -m pip install -r requirements.txt
```

Colab에서 설치할 때는 `%pip install`을 사용하고 패키지를 바꾼 뒤 런타임을 재시작합니다. 모든 실습에 GPU가 필요한 것은 아닙니다. 회귀 신경망 그림의 재현에는 별도의 [실행 안내](reproduce_figures.md)를 따릅니다.

한글 시각화의 준비 셀은 macOS의 AppleGothic 또는 Linux의 NanumGothic을 사용합니다. Colab에 글꼴이 없으면 준비 셀에서 Nanum 글꼴을 설치합니다. 다른 환경에서는 설치한 한글 글꼴의 경로를 지정합니다.

## 읽는 순서

교재와 같은 장·절 체계로 읽습니다. 긴 성능 실험은 본문의 필수 선행 단계가 아니므로 [추가 설명](extended_notes.md)에서 별도로 실행합니다. 데이터 파일 없이 바로 확인하려면 [개념 노트북](../notebooks/2027_concepts.ipynb)을 사용하세요.

이전 Drive Colab 사본은 아래에 남겼습니다. 현재 개정 내용과 대응하는 실행 링크는 저장소 첫 화면의 GitHub 기반 노트북입니다.

- [이전 NumPy Colab](https://colab.research.google.com/drive/1l4_CQ77quYZQ6ylr_hE_-qHfdtnPwCpN)
- [이전 pandas Colab](https://colab.research.google.com/drive/1XcfuJhu2w6jf9ajicDm92ekPsWyrw6SD)
- [이전 시각화 Colab](https://colab.research.google.com/drive/1fc2EnStErqFmcZKyN8S9yUlYtulXbnIT)
