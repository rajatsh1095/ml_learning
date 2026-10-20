import numpy as np


def conv1d(x: np.ndarray, kernel: np.ndarray, mode: str) -> np.ndarray:
    """
    1D cross-correlation ("convolution" in the deep-learning sense: the
    kernel is NOT flipped) with "valid" or "same" zero padding.

    x: shape (n,). kernel: shape (k,), k odd. mode: "valid" or "same".

    "valid": no padding, output length n - k + 1.
    "same": zero-pad x by k // 2 on each side first, output length n.

    Slide the kernel across the (possibly padded) signal without flipping
    it, taking sum(window * kernel) at each position.
    """
    # TODO: build the padded (or unpadded) signal first, then one sliding-window loop.
    if mode == "valid":
        left_padding = 0
        right_padding = 0
    if mode == "same":
        left_padding = kernel.shape[0] //2
        right_padding = kernel.shape[0] - 1 - left_padding

    xp = np.pad(x,(left_padding,right_padding)) # can also use np.concat, or left padding*[0]+ list(x) + right_padding*[0]

    result = []
    for i in range(len(xp)-len(kernel)+1):
        total=0.0
        for j in range(len(kernel)):
            total += xp[i+j]*kernel[j]
        result.append(total)

    return result
    pass
