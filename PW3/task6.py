import pandas as pd
from scipy import stats

# Load the chemical exposure dataset
df = pd.read_csv('PW3/chemicals_cancer.csv')

# Compute correlations with malignancy
benzene_corr, benzene_p = stats.pearsonr(df['benzene'], df['malignancy'])
cadmium_corr, cadmium_p = stats.pearsonr(df['cadmium'], df['malignancy'])

print('--- Naive Analysis: Chemical Associations with Malignancy ---')
print(f'Benzene correlation: {benzene_corr:.4f} (p-value: {benzene_p:.4e})')
print(f'Cadmium correlation: {cadmium_corr:.4f} (p-value: {cadmium_p:.4e})')

# Check correlations with pollution_index and age as well
pollution_corr, _ = stats.pearsonr(df['pollution_index'], df['malignancy'])
age_corr, _ = stats.pearsonr(df['age'], df['malignancy'])
print(f'Pollution index correlation: {pollution_corr:.4f}')
print(f'Age correlation:             {age_corr:.4f}')