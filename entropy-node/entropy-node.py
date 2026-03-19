import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.array(y)
    if len(y) == 0:
        return 0.0
    else:
        _, counts = np.unique(y, return_counts=True)
        p = counts/len(y)
        p = p[p > 0]
        p = np.array(p)
        h = np.sum(p*np.log2(p))*(-1)
        return float(h)