import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    tokens = np.array(tokens)
    vocab = np.array(vocab)
    n = len(vocab)
    res = np.zeros(n, dtype = int)
    for i in range(n):
        res[i] = np.count_nonzero(tokens == vocab[i])

    return res