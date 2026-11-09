import math
import numpy as np

def confidence_calibration_bin(
    probs: list[float], labels: list[int], k: int
) -> list[tuple[int, float, float]]:
    """
    probs: predicted probabilities, each in [0, 1].
    labels: binary true labels (0 or 1), same length as probs.
    k: number of equal-width bins.

    bin(p) = min(k - 1, floor(k * p))

    For each of the k bins (in order 0..k-1), return
    (count, mean_prob, positive_rate). For an empty bin, mean_prob and
    positive_rate are both 0.0.
    """
    # TODO: assign each point to a bin with the clamped formula, then
    # aggregate per bin.
    rets = []
    bins = [[] for _ in range(k)]
    bin_label = [[] for _ in range(k)]
    for i,p in enumerate(probs):
        bin_idx = min(k-1, math.floor(k*p))
        bins[bin_idx].append(p)
        bin_label[bin_idx].append(labels[i])
    for index, bin in enumerate(bins):
        if len(bin) > 0:
            rets.append((len(bin),np.mean(bin),np.mean(np.array(bin_label[index]) ==1)))
        if len(bin) == 0:
            rets.append((0,0,0))

    return rets
            
        
    pass
