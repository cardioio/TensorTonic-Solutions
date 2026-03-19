import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)
    if x.shape == p.shape and abs(np.sum(p)-1)<10**(-6):
        return float(np.sum(x*p))
    else:
        raise ValueError()
        
    
