"""Inputs for the separate synthetic demonstration in steps 13–14 only.

Run from this package's directory, with data/house_data_synthetic.json and
data/location_synthetic.csv present. Continue with the book's model code.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Synthetic teaching data: 40 fictional records, not original practice data.
df_house_demo = pd.read_json("data/house_data_synthetic.json")
df_location_demo = pd.read_csv("data/location_synthetic.csv")
df_demo = pd.merge(df_house_demo, df_location_demo, on="LocationID", how="inner")
df_demo = df_demo[df_demo["District"] != "Unknown"]
df_temp_demo = df_demo[df_demo["Area_Size"] < 500].drop("LocationID", axis=1)
df_na_demo = df_temp_demo.dropna()
df_del_demo = df_na_demo.drop(["Month", "Year"], axis=1)
df_preset_demo = df_del_demo.copy()

X = df_preset_demo.drop("Area_Size", axis=1)
y = df_preset_demo["Area_Size"]
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.2, random_state=42
)
X_train = pd.get_dummies(X_train, dtype=float)
X_valid = pd.get_dummies(X_valid, dtype=float).reindex(
    columns=X_train.columns, fill_value=0
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_valid = scaler.transform(X_valid)
print("Synthetic input shapes:", X_train.shape, X_valid.shape)
