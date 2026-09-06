"""Balanced labelled-context construction used by the B-TabPFN analysis.

The class changes the observations supplied as TabPFN's labelled context. It does
not update pretrained weights, resample query observations, or perform probability
calibration. Model selection and threshold selection belong to the evaluation
protocol in the authoritative notebook.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import Any

import numpy as np


class BalancedContextSampler:
    """Construct deterministic class-balanced contexts without replacement."""

    def __init__(
        self,
        model_factory: Callable[[int], Any],
        n_iter: int = 1,
        random_state: int = 42,
        minority_prevalence: float | None = 0.50,
        fixed_context_n: int | None = None,
    ) -> None:
        self.model_factory = model_factory
        self.n_iter = int(n_iter)
        self.random_state = int(random_state)
        self.minority_prevalence = minority_prevalence
        self.fixed_context_n = None if fixed_context_n is None else int(fixed_context_n)

    def fit(self, X: np.ndarray, y: np.ndarray) -> "BalancedContextSampler":
        X = np.asarray(X)
        y = np.asarray(y, dtype=int)
        if X.shape[0] != y.shape[0]:
            raise ValueError("X and y must contain the same number of observations.")
        if self.n_iter < 1:
            raise ValueError("n_iter must be at least 1.")

        positive = np.flatnonzero(y == 1)
        negative = np.flatnonzero(y == 0)
        if len(positive) == 0 or len(negative) == 0:
            raise ValueError("Both classes are required.")

        minority, majority = (
            (positive, negative) if len(positive) <= len(negative) else (negative, positive)
        )
        natural = len(minority) / len(y)
        desired = natural if self.minority_prevalence is None else float(self.minority_prevalence)
        if not 0 < desired <= 0.5:
            raise ValueError("minority_prevalence must be in (0, 0.5].")

        if self.fixed_context_n is None:
            if abs(desired - natural) < 1e-12:
                minority_n, majority_n = len(minority), len(majority)
            else:
                minority_n = len(minority)
                majority_n = int(round(minority_n * (1 - desired) / desired))
        else:
            minority_n = int(round(self.fixed_context_n * desired))
            majority_n = self.fixed_context_n - minority_n

        if (
            minority_n < 1
            or majority_n < 1
            or minority_n > len(minority)
            or majority_n > len(majority)
        ):
            raise ValueError(
                "Requested context is infeasible: "
                f"minority={minority_n}/{len(minority)}, "
                f"majority={majority_n}/{len(majority)}"
            )

        rng = np.random.RandomState(self.random_state)
        self.X_context_ = X
        self.y_context_ = y
        self.context_indices_: list[np.ndarray] = []
        for _ in range(self.n_iter):
            sampled_minority = (
                minority.copy()
                if minority_n == len(minority)
                else rng.choice(minority, size=minority_n, replace=False)
            )
            sampled_majority = (
                majority.copy()
                if majority_n == len(majority)
                else rng.choice(majority, size=majority_n, replace=False)
            )
            indices = np.concatenate([sampled_minority, sampled_majority])
            rng.shuffle(indices)
            if len(np.unique(indices)) != len(indices):
                raise RuntimeError("Context sampling unexpectedly used replacement.")
            self.context_indices_.append(indices.copy())

        self.context_n_ = minority_n + majority_n
        self.context_minority_n_ = minority_n
        self.context_majority_n_ = majority_n
        self.realized_minority_prevalence_ = minority_n / self.context_n_
        return self

    def iter_fitted_members(
        self, k: int | None = None
    ) -> Iterator[tuple[int, np.ndarray, Any]]:
        if not getattr(self, "context_indices_", None):
            raise RuntimeError("Fit the context constructor first.")
        selected_k = len(self.context_indices_) if k is None else int(k)
        if selected_k < 1 or selected_k > len(self.context_indices_):
            raise ValueError("k must be between 1 and n_iter.")

        for member, indices in enumerate(self.context_indices_[:selected_k]):
            model = self.model_factory(self.random_state + member)
            model.fit(self.X_context_[indices], self.y_context_[indices])
            yield member, indices, model

    def member_probabilities(self, X: np.ndarray, k: int | None = None) -> np.ndarray:
        probabilities = [
            model.predict_proba(np.asarray(X))[:, 1]
            for _, _, model in self.iter_fitted_members(k)
        ]
        return np.vstack(probabilities)

    def predict_proba_at_k(self, X: np.ndarray, k: int | None = None) -> np.ndarray:
        """Return mean two-class scores for the requested number of contexts."""
        selected_k = self.n_iter if k is None else int(k)
        positive_score = self.member_probabilities(X, k=selected_k).mean(axis=0)
        return np.column_stack([1 - positive_score, positive_score])

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Return scores using all contexts constructed by ``fit``."""
        return self.predict_proba_at_k(X, self.n_iter)

    def predict(self, X: np.ndarray, threshold: float = 0.50) -> np.ndarray:
        """Convert positive-class scores to labels at a caller-specified threshold."""
        if not 0 <= threshold <= 1:
            raise ValueError("threshold must be between 0 and 1.")
        return (self.predict_proba(X)[:, 1] >= threshold).astype(int)


ContextEnsemble = BalancedContextSampler
