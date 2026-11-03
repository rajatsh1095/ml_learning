import numpy as np


def temperature_calibrator(z: np.ndarray, tau: float) -> np.ndarray:
    """
    z: logits.
    tau: temperature, tau > 0.

    p = softmax(z / tau), using an overflow-safe softmax (subtract the
    max before exponentiating). Divide by tau, never multiply.

    Return p.
    """
    vals = z/tau
    vals = vals - np.max(vals)
    p = np.exp(vals)/np.exp(vals).sum()
    return p
    # TODO: scale by dividing, then stable softmax.
    pass
