def is_subset(a, b):
    """
    a, b: Python sets

    Returns:
        True if every element of a is also in b (a is a subset of b,
        written a subseteq b), False otherwise.
    """
    # TODO: Implement using Python's own set operations.
    subset = True
    for i in range(len(a)):
        if list(a)[i] in b:
            subset = True
        else:
            subset = False
    return subset
    pass


def argmax(values):
    """
    values: a non-empty list or tuple of numbers

    Returns:
        The INDEX of the largest value in values. If multiple values are
        tied for the maximum, return the first such index.
    """
    # TODO: Implement argmax from Theory: scan once, tracking the best
    # value and its index, updating only on a strictly larger value.
    max_i = 0
    for i in range(len(values)):
        if values[i] > values[max_i]:
            max_i = i
    return max_i            

    pass
