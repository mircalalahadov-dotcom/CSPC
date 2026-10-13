import pandas as pd
import matplotlib.pyplot as plt

columns = [
    "age", "sex", "cp", "trestbps", "chol", "fbs",
    "restecg", "thalach", "exang", "oldpeak",
    "slope", "ca", "thal", "target"
]

df = pd.read_csv(
    "PW3/heart+disease/processed.cleveland.data",
    header=None,
    names=columns,
    na_values="?"
)

variables = ["age", "chol", "trestbps", "thalach"]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

for ax, variable in zip(axes.flat, variables):
    ax.hist(df[variable].dropna(), bins=15, edgecolor="black")
    ax.set_title(variable)
    ax.set_xlabel(variable)
    ax.set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("PW3/distributions.png", dpi=150)
plt.show()
