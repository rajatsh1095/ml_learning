import math
import numpy as np


def perplexity_dashboard(losses: list[float]) -> tuple[float, float]:
    """
    losses: a list of N per-token negative log-likelihood values.

    H = mean(losses)
    PPL = e^H

    Return (mean_loss, perplexity). Exponentiate the MEAN, never the sum.
    """
    # TODO: average first, then exponentiate once.
    mean = np.mean(losses)
    ppl = math.exp(mean)
    print(mean,ppl)
    return mean, ppl
    pass
