def gradient_accumulator(
    theta: float, eta: float, microbatches: list[tuple[int, float]]
) -> tuple[float, float]:
    """
    microbatches: list of (n_j, g_j) pairs, n_j examples with mean
    gradient g_j.

    g = sum(n_j * g_j) / sum(n_j)   (example-weighted mean, NOT the mean
    of the microbatch means).
    theta' = theta - eta * g.

    Return (g, theta_prime).
    """
    # TODO: weight by example count, divide exactly once.
    total = 0
    total_nj = 0
    for (nj, gj) in microbatches:
        total += nj*gj
        total_nj += nj

    g = total/total_nj
    theta = theta - eta*g
    return g,theta
    pass
