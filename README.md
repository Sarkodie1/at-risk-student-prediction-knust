# Explainable At-Risk Student Prediction at KNUST
### Balanced Context Sampling for TabPFN v2 with FSII Explainability

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![TabPFN v2](https://img.shields.io/badge/TabPFN-v2.0.0-orange.svg)](https://github.com/PriorLabs/TabPFN)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXX)

> **Paper:** *"Explainable At-Risk Student Prediction at KNUST: Integrating Academic Behaviour, Mental Health, and Ghana-Specific Contextual Barriers Using TabPFN v2 and Shapley Interaction Values"*
> — Under review, British Journal of Educational Technology (BJET)

---

## Overview

Early warning systems (EWS) in Higher Education struggle to capture how academic performance, mental health symptoms, and Ghana-specific structural barriers **compound** to drive student withdrawal risk. This study addresses three gaps:

| Contribution | Description | Key Result |
|---|---|---|
| **B-TabPFN** | Balanced Context Sampling module for TabPFN v2 inference-time recall recovery | Recall: 0.504 → **0.709** (OOF CV); 0.563 → **0.781** (held-out) |
| **FSII Explainability** | Faithful Shapley Interaction Index reveals sub/super-additive risk interactions | Depressed Mood × Uncontrolled Worry: **sub-additive dampening** (undetectable by SHAP) |
| **External Validation** | UCI Student Dropout benchmark (N=4,424) out-of-distribution robustness | B-TabPFN Recall: **0.825 ± 0.020** — highest among all models |

**Ethics:** Raw KNUST data collected under HuSSREC/AP/544/VOL.5. Public replication uses synthetic data.

---

## Repository Structure

```
at-risk-student-prediction-knust/
│
├── notebooks/
│   └── replication_notebook.ipynb   # All results, tables & figures (outputs cleared)
│                                    # Set USE_RAW_DATA = False → runs on synthetic data
│
├── modules/
│   └── balanced_sampler.py          # Standalone B-TabPFN module (plug-in for any TabPFN workflow)
│
├── data/
│   ├── synthetic_knust_data.csv     # Synthetic N=422 student dataset for public replication
│   └── KNUST_Survey_Schema.md       # Feature codebook: Tinto constructs, scales, descriptives
│
├── requirements.txt                 # Python dependencies (pip install -r requirements.txt)
├── .gitignore                       # Excludes raw data, API keys, large outputs
└── README.md                        # This file
```

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/Sarkodie1/at-risk-student-prediction-knust.git
cd at-risk-student-prediction-knust

# 2. Create environment (Python 3.10 recommended)
conda create -n at_risk_ews python=3.10 -y
conda activate at_risk_ews

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run notebook (uses synthetic data by default)
jupyter notebook notebooks/replication_notebook.ipynb
```

---

## Using B-TabPFN in Your Own Project

The `BalancedContextSampler` is a drop-in wrapper for any TabPFN v2 workflow:

```python
from tabpfn import TabPFNClassifier
from modules.balanced_sampler import BalancedContextSampler

# Standard TabPFN v2 setup
base_clf = TabPFNClassifier(device='cpu')

# Wrap with Balanced Context Sampling (K=20 bootstrap passes, seeds 42+k)
btabpfn = BalancedContextSampler(base_clf=base_clf, n_iter=20, random_state=42)

# Fit and predict (same API as scikit-learn)
btabpfn.fit(X_train, y_train)
probabilities = btabpfn.predict_proba(X_test)   # risk scores for counsellor triage
predictions   = btabpfn.predict(X_test, threshold=0.50)
```

**How it works:** Forces a 1:1 class ratio in each of K in-context attention windows, preventing majority-class dominance from collapsing minority-class recall — without modifying TabPFN's pre-trained weights.

---

## Key Results (KNUST Dataset, N=422)

### 10-Fold Out-of-Fold Cross-Validation (X_train, N=337)

| Model | AUC-ROC | Recall | F2 | Brier |
|---|---|---|---|---|
| Standard TabPFN v2 | 0.755 ± 0.089 | 0.504 | 0.528 | 0.189 |
| **Proposed B-TabPFN** | **0.755 ± 0.089** | **0.709** | **0.683** | 0.199 |
| Logistic Regression | 0.745 ± 0.044 | 0.603 | 0.605 | 0.203 |
| Naive Bayes | 0.773 ± 0.054 | 0.594 | 0.597 | 0.229 |
| XGBoost | 0.660 ± 0.054 | 0.522 | 0.530 | 0.263 |

**Wilcoxon signed-rank test:** W = 0.0 (T⁺ = 55, T⁻ = 0), p = 0.0020, Cohen's d_z = 2.0606, r = 1.000 — B-TabPFN exceeded Standard TabPFN v2 in **all 10 of 10 folds**.

### Held-Out Test Set (X_test, N=85, t=0.50)

| Model | AUC-ROC | Recall | FN count |
|---|---|---|---|
| Standard TabPFN v2 | 0.733 | 0.563 (18/32) | **14 missed** |
| **Proposed B-TabPFN** | **0.734** | **0.781 (25/32)** | **7 missed** |

7 additional at-risk students identified for counsellor follow-up.

---

## Replication Modes

| Mode | Setting | Data | Output |
|---|---|---|---|
| **Public replication** | `USE_RAW_DATA = False` | `synthetic_knust_data.csv` | All code runs; metrics will differ slightly |
| **Exact paper results** | `USE_RAW_DATA = True` | Real KNUST survey (restricted) | Exact figures and tables from paper |

To request the restricted dataset: contact the corresponding author subject to HuSSREC/AP/544/VOL.5 approval.

---

## Ethics & Data Privacy

The raw student survey dataset contains sensitive profiles (mental health indicators, financial difficulty, withdrawal intention) collected under:
- **Ethics approval:** KNUST Humanities and Social Sciences Research Ethics Committee — Reference **HuSSREC/AP/544/VOL.5**
- **Consent:** Written informed consent obtained from all 422 participants
- **Anonymisation:** No PII collected; k-anonymity (k ≥ 5) confirmed for all demographic combinations
- **Governance:** Ghana Data Protection Act (Act 843, 2012)

The raw dataset **is not publicly released**. This repository provides a `synthetic_knust_data.csv` for code verification. Researchers seeking access to the restricted dataset should apply to the corresponding author.

---

## Citation

If you use this code or the B-TabPFN module, please cite:

```bibtex
@article{sarkodie2025btabpfn,
  title   = {Explainable At-Risk Student Prediction at KNUST: Integrating Academic
             Behaviour, Mental Health, and Ghana-Specific Contextual Barriers Using
             TabPFN v2 and Shapley Interaction Values},
  author  = {Sarkodie-Addo, Justice Junior and others},
  journal = {British Journal of Educational Technology},
  year    = {2025},
  note    = {Under review. Code: https://github.com/Sarkodie1/at-risk-student-prediction-knust.
             DOI: 10.5281/zenodo.XXXXXX}
}
```

---

## Requirements

See [`requirements.txt`](requirements.txt). Key packages:

| Package | Version |
|---|---|
| tabpfn | 2.0.0 |
| shapiq | 1.1 |
| scikit-learn | 1.4.0 |
| xgboost | 2.0.0 |
| pandas | 2.0.3 |
| numpy | 1.24.3 |
| matplotlib | 3.7.2 |
| statsmodels | 0.14.0 |

---

## License

This repository is released under the [MIT License](LICENSE). The pre-trained TabPFN v2 weights are subject to the [Prior Labs terms of use](https://github.com/PriorLabs/TabPFN).
