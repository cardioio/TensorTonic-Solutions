def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    res = []
    # Write code here
    for r,v in items:
        wr = v/(v+min_votes)*r + min_votes/(v+min_votes)*global_mean
        res.append(wr)

    return res