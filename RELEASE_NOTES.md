# Release notes

## v1.1.1 — closeout submission revision 6.14.0-closeout

This patch release preserves the v1.1.0 computational protocol and primary results while adding the evidence requested in the final verification report.

### Added and clarified

- Added the full held-out model-comparison grid and tuning-parity evidence.
- Added denominator-complete missingness reporting and explicit false-negative missingness accounting.
- Added the balance-ratio sensitivity grid and leave-one-fold-out K-selection stability analysis.
- Added both requested subgroup tables, with zero-denominator cells retained as not estimable rather than silently removed.
- Added the exact 40% K-selection comparator requested in the closeout support script.
- Added run-integrity and leak-scan evidence, and retained every primary FSII row used in Section 3.4.
- Added a separately labelled ten-seed sensitivity analysis; it is not substituted for the prespecified primary analysis.
- Updated the authoritative executed notebook and public evidence package without exposing restricted row-level data, credentials or checkpoints.

### Reproducibility identity

- Submission revision: `6.14.0-closeout`
- Computational protocol: `6.13.0` (unchanged)
- Protocol hash: `29313c3ae78b30ae423f74d7730651224e950488d1aa84799770ad23a6b841ff`
- Modelling fingerprint: `a8466486d0bfbeeb78bf2191e1df4047d77b528755f5497db77404e3d542a1e0`
- Locked results SHA-256: `b42044a51c23f4f9c7f9b9d8fcb46a83bf959135dbf31445b5fb5e47c80ca756`

The v1.1.0 state remains available through its Git tag, version-specific DOI and repository history.

### Archive

- Version-specific DOI: pending publication
- Concept DOI for the latest version: `10.5281/zenodo.21709992`

## v1.1.0 — authoritative submission revision 6.13.2

This release replaces the v1.0.1/v5.3 repository narrative with the completed, executed submission analysis.

### Changed

- Replaced the cleared legacy notebook with the executed authoritative notebook under the stable name `notebooks/knust_btabpfn_analysis.ipynb`.
- Added the complete public aggregate evidence package under `evidence/v1.1.0/`.
- Corrected the analytic cohort from 422 total responses to 421 eligible undergraduate responses.
- Replaced the legacy K=20 claim with the development-selected K=1 final model while retaining the complete K sensitivity evidence.
- Replaced obsolete performance values with the locked 6.13.2 results.
- Clarified that the outcome is concurrent self-reported withdrawal consideration, not observed future dropout or diagnosis.
- Added the QAPO 2025/2026 undergraduate composition comparison with its non-representativeness limitation.
- Added protocol-bound FSII checkpoint verification and public aggregate FSII summaries.
- Removed obsolete synthetic data, schema summaries, duplicated root figures and the divergent legacy helper.
- Added a standalone helper that matches the final notebook's context-construction semantics.

### Reproducibility identity

- Submission revision: `6.13.2`
- Computational protocol: `6.13.0`
- Protocol hash: `29313c3ae78b30ae423f74d7730651224e950488d1aa84799770ad23a6b841ff`
- Modelling fingerprint: `a8466486d0bfbeeb78bf2191e1df4047d77b528755f5497db77404e3d542a1e0`
- Locked results SHA-256: `985b2accf10f3148f4ecbcfb6a37e086b643a25e6c05128da066636b88b74435`

The prior v1.0.1 state remains available through its Git tag and repository history.

### Archive

- Version-specific DOI: `10.5281/zenodo.22479886`
- Concept DOI for the latest version: `10.5281/zenodo.21709992`
