import numpy as np


def class_weighted_loss(
    logits: np.ndarray, labels: np.ndarray, weights: np.ndarray
) -> float:
    """
    logits: n x C logits.
    labels: length-n 0-based true class indices.
    weights: length-C per-class weights.

    p_ic = softmax(logits_i)_c
    L = -(1/n) * sum_i weights[labels[i]] * log(p_i, labels[i])

    Divide by n, NOT by sum(weights[labels]). Return L.
    """
    # TODO: stable log-softmax per row, weight by true-class weight,
    # sum, divide by n.
    mean_loss = 0
    sfmax = np.exp(logits)/np.exp(logits).sum(axis=1,keepdims=True)
    for i in range(len(logits)):
        nll = -np.log(sfmax[i][labels[i]])
        weighted_loss = nll*weights[labels[i]]
        mean_loss += weighted_loss

    return mean_loss/len(logits)

        
        
    pass
