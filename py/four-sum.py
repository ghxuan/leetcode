from itertools import combinations


def four_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    for i in combinations(nums, 4):
        if sum(i) == target and i not in res:
            res.append(list(i))
    return res


print(four_sum([1, 0, -1, 0, -2, 2], 0))
# [[1, 0, -1, 0], [1, -1, -2, 2], [0, 0, -2, 2]]