import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

# Define column names for the UCI Cleveland Heart Disease dataset
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

# Load the dataset handling missing values marked as '?'
df = pd.read_csv(
    'PW3/heart+disease/processed.cleveland.data',
    header=None,
    names=column_names,
    na_values='?',
)

# Convert target to binary: 0 = healthy, 1 = heart disease (values 1-4)
df['binary_target'] = df['target'].apply(lambda x: 0 if x == 0 else 1)

# Separate thalach values into two groups based on the target
healthy = df[df['binary_target'] == 0]['thalach'].dropna()
disease = df[df['binary_target'] == 1]['thalach'].dropna()

# Compute and print descriptive statistics for both groups
print('--- Group Statistics ---')
print(
    f'Healthy: mean = {healthy.mean():.2f}, SEM = {stats.sem(healthy):.2f},'
    f' std = {healthy.std():.2f}'
)
print(
    f'Disease: mean = {disease.mean():.2f}, SEM = {stats.sem(disease):.2f},'
    f' std = {disease.std():.2f}'
)

# Perform Mann-Whitney U test (appropriate for non-normal distributions)
u_stat, p_val = stats.mannwhitneyu(healthy, disease)
print(f'\nMann-Whitney U test results:')
print(f'  U statistic: {u_stat:.2f}')
print(f'  p-value:     {p_val:.4e}')

# Create a bar plot showing means and uncertainty (standard error)
groups = ['Healthy (0)', 'Heart Disease (1)']
means = [healthy.mean(), disease.mean()]
errors = [stats.sem(healthy), stats.sem(disease)]

plt.figure(figsize=(8, 6))
plt.bar(
    groups, means, yerr=errors, capsize=5, color=['skyblue', 'salmon'], alpha=0.8
)
plt.ylabel('Maximum Heart Rate (thalach)')
plt.title('Comparison of Max Heart Rate between Healthy and Diseased Patients')
plt.ylim(0, 200)

# Add numerical labels on top of the bars
for i, v in enumerate(means):
  plt.text(i, v + 10, f'{v:.1f}', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('PW3/thalach_comparison.png', dpi=300)
print('\nFigure successfully saved to PW3/thalach_comparison.png')