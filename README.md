# Explainable At-Risk Student Prediction at KNUST: Integrating Academic Behaviour, Mental Health, and Ghana-Specific Contextual Barriers Using TabPFN v2 and Shapley Interaction Values

This repository contains the replication code, standalone modules, and synthetic data for the research project:
*"Explainable At-Risk Student Prediction at KNUST: Integrating Academic Behaviour, Mental Health, and Ghana-Specific Contextual Barriers Using TabPFN v2 and Shapley Interaction Values"*.

---

## 1. Project Overview

Early warning systems (EWS) in Higher Education often struggle to capture how academic, mental health, and structural barriers compound to drive student withdrawal risk. This study addresses these gaps through three contributions:
1.  **TabPFN v2 Application:** We apply TabPFN v2—a tabular foundation model—to predict at-risk status using student survey data from Kumasi, Ghana.
2.  **Recall Recovery (B-TabPFN):** To resolve TabPFN's minority-class recall deficit under class imbalance, we deploy a **Balanced Context Sampling** module (`B-TabPFN`), which recovers recall (0.504 to 0.709) without degrading overall discriminative performance.
3.  **FSII Interaction Explainability:** We deploy the **Faithful Shapley Interaction Index (FSII)** via the `shapiq` library to reveal sub-additive and super-additive risk factor interactions (such as the sub-additive relationship between depressed mood and worry).

---

## 2. Directory Structure

```
at-risk-student-prediction-knust/
├── modules/
│   └── balanced_sampler.py      # Standalone B-TabPFN module
├── notebooks/
│   └── replication_notebook.ipynb  # Jupyter Notebook for all results, tables, and figures
├── data/
│   ├── KNUST_Survey_Schema.md   # Feature dictionary and survey scale mappings
│   └── synthetic_knust_data.csv # Synthetic student dataset (N=422) for public replication
├── requirements.txt             # Python package dependencies
└── README.md                    # This documentation file
```

---

## 3. Installation

We recommend using a clean virtual environment (conda or venv) running Python 3.10:

```bash
# Clone the repository
git clone https://github.com/Sarkodie1/at-risk-student-prediction-knust.git
cd at-risk-student-prediction-knust

# Create and activate environment
conda create -n at_risk_ews python=3.10 -y
conda activate at_risk_ews

# Install dependencies
pip install -r requirements.txt
```

---

## 4. Usage: Balanced Context Sampler (B-TabPFN)

You can import and use the `BalancedContextSampler` module in any standard scikit-learn workflow with TabPFN:

```python
from tabpfn import TabPFNClassifier
from modules.balanced_sampler import BalancedContextSampler

# Initialize base classifier (TabPFN v2)
base_clf = TabPFNClassifier(device='cpu')

# Initialize the Balanced Context Sampler (K=20 bootstrap passes)
btabpfn = BalancedContextSampler(base_clf=base_clf, n_iter=20, random_state=42)

# Fit context window and predict
btabpfn.fit(X_train, y_train)
probabilities = btabpfn.predict_proba(X_test)
predictions = btabpfn.predict(X_test, threshold=0.5)
```

---

## 5. Replicating Results

To replicate all figures, tables, and metrics in the paper:
1.  Navigate to the `notebooks/` directory.
2.  Open `replication_notebook.ipynb` in your Jupyter environment.
3.  By default, `USE_RAW_DATA = False` is set at the top of the data-loading cell, which runs the pipeline on the public `synthetic_knust_data.csv` to verify that all code compiles.
4.  To replicate the exact figures in the paper, change `USE_RAW_DATA = True` (requires placing the restricted raw dataset `knust_real_data.csv` in your downloads directory).

---

## 6. Ethics and Data Privacy

The raw student survey dataset contains sensitive student profiles (including financial difficulties and mental health indicators) collected under ethical clearance from the Humanities and Social Sciences Research Ethics Committee (HuSSREC) at KNUST (Reference: **HuSSREC/AP/544/VOL. 5**). 

To comply with ethics board guidelines and protect participant privacy, the raw dataset is not public. Researchers requesting access to the raw data must apply to the corresponding author, subject to HuSSREC administrative approval.
