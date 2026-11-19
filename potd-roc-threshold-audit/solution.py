def roc_threshold_audit(
    probs: list[float], labels: list[int], tau: float
) -> tuple[int, int, int, int, float, float]:
    """
    probs: predicted probabilities.
    labels: binary true labels (0 or 1), same length as probs.
    tau: decision threshold. Predict positive iff p_i >= tau.

    Returns (TP, FP, TN, FN, precision, recall).
    precision = TP / (TP + FP), or 0 if that denominator is 0.
    recall = TP / (TP + FN), or 0 if that denominator is 0.
    """
    # TODO: tally the confusion matrix, then compute precision and recall.
    tp = fp = tn = fn = 0
    for i in range(len(probs)):
        if probs[i] >= tau:
            if labels[i] == 1:
                tp +=1
            else:
                fp +=1
        else:
            if labels[i] == 0:
                tn +=1
            else:
                fn +=1
    precision = tp/(tp+fp) if tp+fp > 0 else 0
    recall = tp/(tp+fn) if tp+fn > 0 else 0
    return  tp, fp,tn, fn, precision, recall
    pass
