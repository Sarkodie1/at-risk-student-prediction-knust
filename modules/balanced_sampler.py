"""
Balanced Context Sampler for TabPFN v2 (B-TabPFN)
Author: Sarkodie-Addo Justice Junior
"""

import numpy as np
import copy


class BalancedContextSampler:
    """
    BalancedContextSampler modifies TabPFN's inference by constructing multiple 
    balanced context windows. This addresses recall deficits caused by majority-class 
    dominance in imbalanced tabular datasets.

    Parameters
    ----------
    base_clf : object
        An unfitted TabPFN classifier instance.
    n_iter : int, default=20
        Number of bootstrap balanced-context iterations.
    random_state : int, default=42
        Reproducibility seed.
    """

    def __init__(self, base_clf, n_iter=20, random_state=42):
        self.base_clf = base_clf
        self.n_iter = n_iter
        self.random_state = random_state
        self.rng_ = np.random.RandomState(random_state)
        self._fitted_clfs = []

    def fit(self, X_ctx, y_ctx):
        """
        Build K balanced context windows. No parameters are updated; this is pure 
        in-context data composition.
        """
        self._pos_idx = np.where(y_ctx == 1)[0]
        self._neg_idx = np.where(y_ctx == 0)[0]
        self._fitted_clfs = []
        n_pos = len(self._pos_idx)
        
        for _ in range(self.n_iter):
            neg_sample = self.rng_.choice(self._neg_idx, size=n_pos, replace=False)
            ctx_idx = np.concatenate([self._pos_idx, neg_sample])
            self.rng_.shuffle(ctx_idx)
            
            clf_i = copy.deepcopy(self.base_clf)
            clf_i.fit(X_ctx[ctx_idx], y_ctx[ctx_idx])
            self._fitted_clfs.append(clf_i)
        return self

    def predict_proba(self, X):
        """
        Aggregate predicted probabilities across all balanced context passes.
        """
        proba = np.zeros((len(X), 2))
        for clf_i in self._fitted_clfs:
            proba += clf_i.predict_proba(X)
        return proba / self.n_iter

    def predict(self, X, threshold=0.5):
        """
        Classify instances based on a decision threshold.
        """
        return (self.predict_proba(X)[:, 1] >= threshold).astype(int)
