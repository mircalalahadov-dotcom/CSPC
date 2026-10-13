import pandas as pd
from scipy import stats

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

continuous_vars = ['age', 'chol', 'trestbps', 'thalach']

print('--- Результаты теста Шапиро-Уилка на нормальность ---')
print('(Если p-value < 0.05, то распределение не является нормальным)\n')

for var in continuous_vars:
  data = df[var].dropna()
  stat, p_value = stats.shapiro(data)
  skew = data.skew()
  print(f'Переменная: {var}')
  print(f'  Статистика: {stat:.4f}')
  print(f'  p-значение: {p_value:.4e}')
  print(f'  Асимметрия: {skew:.4f}\n')
