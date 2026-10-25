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
    
    for i in range(scores.shape[0]):
        for j in range(scores.shape[1]):
            if j>i:
                scores[i][j] = -np.inf
        max_score = np.max(scores[i])
        scores[i] = scores[i] - max_score

        exps = np.exp(scores[i])
        total = np.sum(exps)
        print(exps, total)
        scores[i] = exps/total
    return scores
    pass
