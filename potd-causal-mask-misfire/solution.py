import numpy as np


def causal_mask_misfire(scores: np.ndarray) -> np.ndarray:
    """
    Row-wise, numerically stable softmax under a causal mask: for query
    row i, only key columns j <= i are visible. Forbidden entries (j > i)
    must be exactly 0.0 in the output.

    scores: shape (n, n).
    """
    # TODO: mask with -inf BEFORE taking the row max, so forbidden entries
    # never influence the max-subtraction or the normalizer.
    
    n = scores.shape[0]

    for i in range(n):
        scores[i, i+1:] = -np.inf

        max_score = np.max(scores[i])
        exps = np.exp(scores[i] - max_score)

        scores[i] = exps / np.sum(exps)

    return scores
    pass
