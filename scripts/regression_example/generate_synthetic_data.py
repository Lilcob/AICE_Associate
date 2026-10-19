"""Create the 40-row synthetic input used only for the book's steps 13–14.

These are fictional teaching data, not observed housing records and not a
reconstruction of the unavailable original practice files.
"""
from pathlib import Path
import argparse
import json
import hashlib

import numpy as np
import pandas as pd


def create_data(out: Path):
    out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(2027)
    n = 40
    districts = np.array(["Seoul", "Gyeonggi", "Incheon"])
    building_types = np.array(["Apartment", "Villa", "Office"])
    location_id = np.arange(1, n + 1)
    year_built = rng.integers(1990, 2024, size=n)
    rooms = rng.integers(1, 6, size=n)
    bathrooms = rng.integers(1, 4, size=n)
    floor = rng.integers(1, 25, size=n)
    distance = rng.integers(100, 1501, size=n)
    district_index = rng.integers(0, len(districts), size=n)
    building_index = rng.integers(0, len(building_types), size=n)
    parking = rng.integers(0, 2, size=n)
    school_count = rng.integers(0, 6, size=n)
    # A deliberately invented relationship for demonstrating model.fit.
    # Coefficients are not empirical claims about housing markets.
    area = (
        20 + 13 * rooms + 8 * bathrooms + 0.25 * floor
        - 0.002 * distance + 0.08 * (year_built - 1990)
        + np.array([5, 2, -3])[district_index]
        + np.array([8, -4, -8])[building_index]
        + 2 * parking + 0.8 * school_count + rng.normal(0, 4, size=n)
    ).round(3)
    house = pd.DataFrame({
        "Area_Size": area, "Year_Built": year_built, "Rooms": rooms,
        "Bathrooms": bathrooms, "Floor_Level": floor,
        "Distance_Subway": distance, "District": districts[district_index],
        "Building_Type": building_types[building_index], "Parking": parking,
        "Month": rng.integers(1, 13, size=n),
        "Year": np.full(n, 2026), "LocationID": location_id,
    })
    location = pd.DataFrame({"LocationID": location_id, "School_Count": school_count})
    assert len(house) == len(location) == 40
    assert not house.isna().any().any()
    assert house.Area_Size.between(0, 499.999).all()
    # Deliberately distinct filenames prevent confusion with original data.
    house_path = out / "house_data_synthetic.json"
    location_path = out / "location_synthetic.csv"
    house.to_json(house_path, orient="records", indent=2, force_ascii=False, double_precision=3)
    location.to_csv(location_path, index=False)
    metadata = {
        "provenance": "synthetic", "purpose": "Steps 13–14 neural-network training/learning-curve demonstration only",
        "observed_real_estate_records": False, "reconstruction_of_original_data": False,
        "generator": "generate_synthetic_data.py", "numpy_generator": "default_rng(2027)",
        "rows_per_input_file": 40, "merged_rows": 40,
        "missing_cells": 0, "unknown_district_rows": 0,
        "area_filter_excluded_rows": 0, "area_range": [float(area.min()), float(area.max())],
        "target_rule_note": "Invented numeric formula plus Normal(0,4) noise; see source code. No housing-market interpretation.",
        "files": [{"name": p.name, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
                  for p in (house_path, location_path)],
    }
    (out / "synthetic_data_manifest.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(metadata, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path(__file__).parent / "data")
    create_data(parser.parse_args().out)
