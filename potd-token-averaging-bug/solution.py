import numpy as np


def valid_token_mean_loss(losses: np.ndarray, mask: np.ndarray) -> float:
    """
    losses: B x T array of per-token losses.
    mask: B x T array of 0/1 validity flags (same shape as losses).

    L = sum(mask * losses) / sum(mask)

    If sum(mask) == 0, return 0.0 (no division by zero).

    Return L as a float.
    """
    # TODO: sum only over valid tokens, in both numerator and denominator.
    total_loss = losses * mask
    #print(total_loss)
    total_loss = np.sum(total_loss)
    non_zero = np.count_nonzero(mask)
    non_zero = 1 if non_zero == 0 else non_zero
    #print(total_loss, non_zero)
    total_loss_avg = total_loss/non_zero
    #print(total_loss_avg)
    return total_loss_avg
    pass
