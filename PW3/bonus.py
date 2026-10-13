import pandas as pd

# Load heart dataset
column_names = [
    'age',
    'sex',
    'cp',
    'trestbps',
    'chol',
    'fbs',
    'restecg',
    'thalach',
    'exang',
    'oldpeak',
    'slope',
    'ca',
    'thal',
    'target',
]

df = pd.read_csv(
    'PW3/heart+disease/processed.cleveland.data',
    header=None,
    names=column_names,
    na_values='?',
)

# Binary target proportions
df['binary_target'] = df['target'].apply(lambda x: 0 if x == 0 else 1)
proportions = df['binary_target'].value_counts(normalize=True)

print('--- Target Proportions (Bonus Task) ---')
print(proportions)
