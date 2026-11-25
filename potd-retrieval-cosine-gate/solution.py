import numpy as np


def retrieval_cosine_gate(query: np.ndarray, documents: np.ndarray) -> np.ndarray:
    """
    query: array of shape (d,).
    documents: array of shape (n, d).

    Returns an array of shape (n,): cosine similarity between query and
    each document row. If either the query or a document has zero norm,
    that document's similarity is 0.
    """
    # TODO: compute dot(query, doc) / (||query|| * ||doc||) per document,
    # guarding against zero norms.
    res = []
    for i in documents:
        deno = (np.sqrt(np.sum(np.square(query)))*np.sqrt(np.sum(np.square(i))))
        if deno == 0:
            res.append(0)
        else:
            res.append((np.sum(query*i))/deno)
    return res
        
    
    pass
