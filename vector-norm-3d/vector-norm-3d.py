import numpy as np

def vector_norm_3d(v):
    v = np.array(v)
    
    if v.ndim == 1:
        # 如果是一维 [3, 4, 12]，直接计算，返回标量
        return np.linalg.norm(v)
    else:
        # 如果是多维 [[3, 4, 12], ...]，按行计算，返回数组
        return np.linalg.norm(v, axis=-1)