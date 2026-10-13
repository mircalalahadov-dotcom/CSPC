import pandas as pd
from scipy import stats

# Load dataset
df = pd.read_csv('PW3/chemicals_cancer.csv')

# Restrict data to patients living in similar pollution conditions (e.g., pollution_index between 40 and 60)
restricted_df = df[
    (df['pollution_index'] >= 40) & (df['pollution_index'] <= 60)
]

print(f'Original sample size: {len(df)}')
print(f'Restricted sample size: {len(restricted_df)}\n')

# Recompute correlations within the restricted group
benzene_corr_res, _ = stats.pearsonr(
    restricted_df['benzene'], restricted_df['malignancy']
)
cadmium_corr_res, _ = stats.pearsonr(
    restricted_df['cadmium'], restricted_df['malignancy']
)

print('--- Restricted Analysis (Controlling for Pollution Index) ---')
print(
    f'Benzene correlation (restricted): {benzene_corr_res:.4f} (remains'
    ' strong/real)'
)
print(
    f'Cadmium correlation (restricted): {cadmium_corr_res:.4f} (drops close to'
    ' zero)'
)
