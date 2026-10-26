import numpy as np


def label_smoothing(logits: np.ndarray, y: int, eps: float) -> tuple[np.ndarray, float]:
    """
    Build the label-smoothed target distribution over C = len(logits)
    classes and compute its cross-entropy loss against logits.

    q[c] = 1 - eps + eps/C for c == y, else eps/C.
    loss = -sum(q * log_softmax(logits)).

    Return (q, loss).
    """
    # TODO: smooth EVERY class by eps/C first, then add the remaining
    # mass (1 - eps) onto the true class y.
    logits = logits - np.max(logits)
    log_prob = logits - np.log(np.exp(logits).sum())
    target = np.full(len(logits), eps/len(logits))
    target[y] += 1-eps 
    loss = -np.sum(target*log_prob)
    return target, loss
    pass
