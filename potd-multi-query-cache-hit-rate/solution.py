def cache_hit_rate(keys: list[int]) -> tuple[int, int, float]:
    """
    keys: a sequence of request keys in arrival order.

    A request is a hit iff its key has appeared earlier in the sequence
    (the first occurrence of any key is always a miss).

    Return (hits, misses, rate) where rate = hits / len(keys).
    """
    # TODO: track which keys have been seen so far, in order.
    if len(keys) == 0:
        return [0,0,0]
    count_misses = len(set(keys))
    hits = len(keys) - count_misses
    rate = hits/len(keys)
    return [hits, count_misses, rate]
    
    pass
