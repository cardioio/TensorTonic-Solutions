def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # 1. 确保取前 k 个推荐项 (假设 recommended 是 list 或 1D array)
    top_k = recommended[:k]
    
    # 2. 计算交集 (使用 & 或 .intersection 均可)
    # 转换为 set 可以去重并加速查找
    relevant_set = set(relevant)
    hits = set(top_k).intersection(relevant_set)
    
    n_hits = len(hits)
    
    # 3. 计算指标
    # Precision@k = 相关且在前k个 / k
    precision = n_hits / k if k > 0 else 0
    
    # Recall@k = 相关且在前k个 / 总相关数
    recall = n_hits / len(relevant_set) if len(relevant_set) > 0 else 0
    
    return [precision, recall]