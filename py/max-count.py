def maxCount(m, n, ops):
    """
    :type m: int
    :type n: int
    :type ops: List[List[int]]
    :rtype: int
    """
    res = list(zip(*ops))
    return min(res[0])*min(res[1])


print(maxCount(3, 3, [[2, 2], [3, 3]]))
# 4