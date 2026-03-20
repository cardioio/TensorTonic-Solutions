import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    if len(rater1) != len(rater2):
        raise ValueError("长度不相等")

    rater1 = np.array(rater1)
    rater2 = np.array(rater2)

    n = len(rater1)
    p0 = np.count_nonzero(rater1 == rater2) / n

    labels = np.union1d(rater1, rater2)
    pe = 0.0

    for label in labels:
        p1 = np.sum(rater1 == label) / n
        p2 = np.sum(rater2 == label) / n
        pe += p1 * p2

    if 1 - pe == 0:
        return 1.0

    return float((p0 - pe) / (1 - pe))