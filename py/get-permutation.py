def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    if n is 1: return '1'
    jie, res_str, res = [1], '', [i for i in range(1, n + 1)]
    for i in res[1:-1]:
        jie.append(i * jie[-1])
    # k 需要自减一，因为列表的索引是从 0 开始的，不是从一开始的
    k -= 1
    for i in jie[::-1]:
        pop, k = divmod(k, i)
        res_str += str(res.pop(pop))
    res_str += str(res.pop(0))
    return res_str


print(getPermutation(1, 1))
print(getPermutation(3, 3))
print(getPermutation(4, 9))
# 1
# 213
# 2314
