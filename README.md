# B-TabPFN for student-support screening at KNUST

This repository contains the executed analysis notebook and public verification evidence for:

**Balanced Context Sampling for TabPFN v2: Explainable Concurrent Identification of Withdrawal Consideration among KNUST Undergraduates**

Repository release **v1.1.1** corresponds to closeout submission revision **6.14.0-closeout** and computational protocol **6.13.0**. The closeout release adds the supervisor-requested reporting checks and a separately labelled ten-seed sensitivity analysis; it does not change the prespecified model, partition, operating threshold or primary FSII protocol. Release v1.1.0 remains the archived pre-closeout state.

## Study scope

The KNUST study is a cross-sectional, concurrent screening analysis. Its target is students' self-reported consideration of withdrawal or a semester break during the survey period. It does not measure observed future dropout, make a clinical diagnosis, or justify automated counselling decisions.

The survey received 422 responses. One postgraduate response was excluded from the undergraduate primary analysis, leaving 421 records: 159 positive-target responses (37.8%) and 262 negative-target responses. A fixed stratified split assigned 336 records to development and 85 to a held-out secondary evaluation.

Recruitment was voluntary and non-probability-based. The QAPO comparison describes differences between the achieved sample composition and the 2025/2026 registered undergraduate population; it does not establish representativeness or an institution-wide prevalence estimate.

## Proposed method

B-TabPFN changes the labelled inference context supplied to a frozen TabPFN v2 model. It retains all available minority-class development observations and samples an equal number of majority-class observations without replacement. Pretrained weights and query observations are unchanged.

Candidate context counts, K = 1, 5, 10, 15 and 20, were evaluated using development data. The declared one-standard-error rule selected the smallest eligible model, **K=1**. K=15 had the highest mean development F2 and is retained as sensitivity evidence rather than substituted after inspection of the held-out outcomes.

## Principal results

At the fixed 0.50 operating threshold:

| Evaluation | Model | Precision | Recall | F1 | F2 | AUROC | Average precision |
|---|---|---:|---:|---:|---:|---:|---:|
| Nested development OOF (pooled) | Standard TabPFN v2 | 0.639 | 0.488 | 0.554 | 0.512 | 0.753 | 0.639 |
| Nested development OOF (pooled) | B-TabPFN | 0.585 | 0.677 | 0.628 | 0.656 | 0.752 | 0.644 |
| Held-out secondary evaluation | Standard TabPFN v2 | 0.655 | 0.594 | 0.623 | 0.605 | 0.746 | 0.654 |
| Held-out secondary evaluation | B-TabPFN K=1 | 0.605 | 0.719 | 0.657 | 0.693 | 0.743 | 0.618 |

The Nadeau-Bengio corrected mean outer-fold recall difference was 0.188 (95% CI 0.095 to 0.282; two-sided p=0.0014). The exact held-out McNemar comparison between B-TabPFN and standard TabPFN at 0.50 was not statistically significant (p=1.000). These results support a recall-oriented screening trade-off in this surveyed cohort, not a claim of universally superior discrimination.

Primary FSII summaries cover the 32 positive-target students in the held-out partition, use a budget of 1024, and explain the exact final K=1 positive-class score. The UCI experiment is a separate algorithmic robustness benchmark with a different outcome construct; it is not external validation of the KNUST screening instrument.

## Repository contents

```text
notebooks/
  knust_btabpfn_analysis.ipynb   executed authoritative notebook
modules/
  balanced_context.py           reusable context-construction helper
evidence/v1.1.1/
  aggregate tables, diagnostics, manifests and publication figures
requirements.txt                explicit packages installed by the notebook
RELEASE_NOTES.md                release-to-protocol mapping and migration notes
```

The concise notebook filename is stable across future releases. Version identity is recorded by the Git tag and by `evidence/v1.1.1/submission_release.json`.

## Reproduction and verification

The executed notebook preserves displayed outputs. Exact rerunning requires:

- a Colab 2026.07 Python 3.12 GPU runtime;
- the restricted row-level KNUST CSV;
- the protocol-bound private FSII checkpoints for a submission rerun; and
- a TabPFN credential supplied through a Colab Secret named `TABPFN_TOKEN`.

The credential, raw survey, row-level predictions and private checkpoints must never be committed. The notebook verifies the raw-data hash, partitions, modelling code, current model probabilities, checkpoint protocol, interaction completeness and reconstruction error before accepting saved FSII work.

The public evidence package permits review of aggregate results without exposing sensitive student-level data. Start with:

- [`results_manifest.json`](evidence/v1.1.1/results_manifest.json) for the authoritative run identity and completion state;
- [`claims_evidence_source.csv`](evidence/v1.1.1/claims_evidence_source.csv) for claim-to-artifact traceability;
- [`decision_provenance_register.csv`](evidence/v1.1.1/decision_provenance_register.csv) for analysis decisions;
- [`run_status_dashboard.csv`](evidence/v1.1.1/run_status_dashboard.csv) for component completion;
- [`warning_summary.csv`](evidence/v1.1.1/warning_summary.csv) for classified compatibility notices;
- [`closeout_verdict.csv`](evidence/v1.1.1/closeout_verdict.csv) for the six closeout conditions; and
- [`artifact_manifest.csv`](evidence/v1.1.1/artifact_manifest.csv) for artifact hashes.

The full Colab base image reports conflicts involving unused preinstalled packages. The imported analysis stack is separately version-checked and functionally tested in the notebook; see `pip_check.json`, `resolved_analysis_versions.json` and `tabpfn_integration_probe.json`.

## Data governance and ethics

Ethics approval reference: **HuSSREC/AP/544/VOL.5**.

Only aggregate or disclosure-controlled evidence is public. The repository does not contain the raw KNUST survey, the ethics letter, the QAPO source form, private FSII checkpoints or row-level model outputs. Requests for restricted data require separate ethical and institutional authorization.

## Archive

- Version-specific v1.1.1 archive: **pending publication of this release on Zenodo**
- Pre-closeout v1.1.0 archive: [DOI 10.5281/zenodo.22479886](https://doi.org/10.5281/zenodo.22479886)
- Latest-version archive: [Zenodo concept DOI 10.5281/zenodo.21709992](https://doi.org/10.5281/zenodo.21709992)

Use the version-specific DOI when citing an exact analysis release. The concept DOI resolves to the latest archived repository version.

## Software notice

No repository-wide software licence is asserted by this release. TabPFN code and pretrained weights remain subject to their respective upstream terms.
