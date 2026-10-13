import matplotlib.pyplot as plt
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

# Load the dataset
df = pd.read_csv(
    'PW3/heart+disease/processed.cleveland.data',
    header=None,
    names=column_names,
    na_values='?',
)

# Extract age and thalach, dropping missing values
data_subset = df[['age', 'thalach']].dropna()
age = data_subset['age']
thalach = data_subset['thalach']

# Compute Pearson correlation coefficient and p-value
corr, p_value = stats.pearsonr(age, thalach)
print('--- Age and Thalach Correlation ---')
print(f'Pearson correlation coefficient: {corr:.4f}')
print(f'p-value:                        {p_value:.4e}')

# Create a scatter plot to visualize the relationship
plt.figure(figsize=(8, 6))
plt.scatter(age, thalach, alpha=0.7, edgecolor='k')
plt.title('Relationship Between Age and Maximum Heart Rate (thalach)')
plt.xlabel('Age (years)')
plt.ylabel('Maximum Heart Rate (thalach)')

# Add a linear trendline (best fit line)
m, b = pd.np.polyfit(age, thalach, 1) if hasattr(pd, 'np') else __import__('numpy').polyfit(age, thalach, 1)
plt.plot(age, m * age + b, color='red', linewidth=2, label=f'Trendline (r = {corr:.2f})')
plt.legend()

plt.tight_layout()
plt.savefig('PW3/age_thalach_scatter.png', dpi=300)
print('\nFigure successfully saved to PW3/age_thalach_scatter.png')
