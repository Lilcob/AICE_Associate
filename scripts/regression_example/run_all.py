"""Generate the fixed synthetic inputs and reproduce all figure/log artifacts."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
subprocess.run([sys.executable, str(root / "generate_synthetic_data.py"),
                "--out", str(root / "data")], check=True)
subprocess.run([
    sys.executable, str(root / "reproduce_curve.py"),
    "--house", str(root / "data/house_data_synthetic.json"),
    "--location", str(root / "data/location_synthetic.csv"),
    "--out", str(root / "run"), "--provenance", "synthetic",
    "--source-note", "재현용 합성 데이터 40행: 단계 13·14 신경망 문법 시연. 원자료나 실제 부동산 관측자료의 결과가 아닙니다.",
    "--repeat-check",
], check=True)
