import pandas as pd

columns = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
    "target",
]

df = pd.read_csv(
    "PW3/heart+disease/processed.cleveland.data",
    header=None,
    names=columns,
    na_values="?"
)

continuous = ["age", "chol", "trestbps", "thalach"]

print("Dataset shape:", df.shape)
print("\nFirst five rows:")
print(df.head())

print("\nContinuous variables:")
print(df[continuous].head())

print("\nSummary statistics:")
print(df[continuous].describe())

print("\nMissing values:")
print(df[continuous].isnull().sum())
