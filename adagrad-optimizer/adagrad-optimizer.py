import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Write code here
    # Zero gradient means no parameter update and G stays unchanged    
    new_G = G + np.power(g,2)
    new_w = w - lr/np.sqrt(new_G +eps)*g
    return (new_w,new_G)
    