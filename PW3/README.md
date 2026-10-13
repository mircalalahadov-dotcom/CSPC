# Practical Work 3 (PW3) Report

This repository contains the complete end-to-end statistical analysis, data characterization, hypothesis testing, and causal inference investigations for **Practical Work 3 (PW3)** in the *Computer Science for Physics and Chemistry* course.

---

## Session 1: Characterise the Data & Normality

### 1. Data Loading & Inspection
* **Dataset 1:** UCI Cleveland Heart Disease dataset (`processed.cleveland.data`), containing 303 rows and 14 clinical attributes.
* **Continuous Variables Analyzed:** 
  * `age` (Age in years)
  * `chol` (Serum cholesterol in mg/dl)
  * `trestbps` (Resting blood pressure in mm Hg on admission)
  * `thalach` (Maximum heart rate achieved)

### 2. The Shape of Each Variable (`distributions.png`)
* **`age`**: Approximately bell-shaped and symmetric, centered around the late 50s, indicating that the dataset primarily samples middle-aged and older adults.
* **`chol`**: Right-skewed distribution, with most values concentrated between 200 and 300 mg/dl and a few elevated outlier values extending past 500 mg/dl.
* **`trestbps`**: Unimodal, right-skewed distribution where most patients cluster around 120–140 mm Hg, accompanied by a gradual tail toward higher blood pressures.
* **`thalach`**: Roughly symmetric and unimodal distribution, peaking between 150 and 160 bpm.

### 3. Normality Tests (Shapiro-Wilk)
* **`age`**: Statistic = 0.9865, $p$-value = 6.07e-03 (Skewness: -0.21)
* **`chol`**: Statistic = 0.9473, $p$-value = 5.91e-09 (Skewness: 1.14)
* **`trestbps`**: Statistic = 0.9665, $p$-value = 1.80e-06 (Skewness: 0.71)
* **`thalach`**: Statistic = 0.9765, $p$-value = 7.00e-05 (Skewness: -0.54)
* *Note:* Due to large sample sizes and minor real-world variations, all variables reject strict normality ($p < 0.05$). However, visual inspections (`age` and `thalach`) justify parametric-like treatment or non-parametric validation.

---

## Session 2: Draw Conclusions

### 4. Is the Effect Real? (`thalach_comparison.png`)
* **Finding:** Patients without heart disease (`target = 0`) exhibit a significantly higher mean maximum heart rate ($158.38 \pm 1.50$ bpm) compared to patients diagnosed with heart disease ($139.26 \pm 1.92$ bpm).
* **Statistical Test:** Non-parametric Mann-Whitney U test yielded $U = 16989.50$ with a highly significant $p$-value ($1.86 \times 10^{-13}$), proving the effect is genuine and robust.

### 5. Do Two Things Move Together? (`age_thalach_scatter.png`)
* **Finding:** Age and maximum heart rate (`thalach`) exhibit a moderate negative correlation (Pearson's $r \approx -0.3938$, $p \approx 1.11 \times 10^{-12}$). As age increases, the maximum heart rate achieved during exercise decreases, reflecting natural physiological decline.

---

## Dataset 2: The Chemical-Exposure Mystery (`chemicals_cancer.csv`)

### 6. The Naive Analysis
* **Variables:** 1000 samples evaluating `benzene`, `cadmium`, `pollution_index`, `age`, and tumor `malignancy`.
* **Initial Correlations:**
  * Benzene vs Malignancy: $r \approx 0.3847$ ($p = 1.28 \times 10^{-36}$)
  * Cadmium vs Malignancy: $r \approx 0.8800$ ($p \approx 0$)
  * Pollution Index vs Malignancy: $r \approx 0.8951$
* **Naive Conclusion:** At face value, **cadmium** shows an exceptionally high direct correlation and appears to be the primary cause of cancer.

### 7. The Confounding Variable Revealed
* **Analysis:** Controlling for the confounding variable (`pollution_index`) by restricting the dataset to a narrow exposure range ($40 \le \text{pollution\_index} \le 60$, reducing sample size to 201):
  * Benzene correlation (restricted): $r \approx 0.6979$ (remains strong and true)
  * Cadmium correlation (restricted): $r \approx 0.3132$ (drops significantly)
* **Final Conclusion:** **Benzene** is the true cause of tumour malignancy. **Cadmium** only appeared guilty due to confounding by regional environmental pollution (`pollution_index`).

### Bonus: Target Balance
* **Proportions:** Healthy (`0`): ~54.1%, Heart Disease (`1`): ~45.9%. The dataset is well-balanced for binary classification tasks.
