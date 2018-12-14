from itertools import combinations


def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums)
    nums_ = nums[::-1]
    res = []
    count = nums.count(0)
    minus = nums[:nums.index(0)]
    plus = nums_[:nums_.index(0)]
    if count >= 1:
        for i in set(plus):
            if -i in minus:
                res.append([0, i, -i])
        if count >= 3:
            res.append([0] * 3)
    for i in combinations(plus, 2):
        if -sum(i) in minus:
            res.append(list(i)+[-sum(i)])
    for i in combinations(minus, 2):
        if -sum(i) in plus:
            res.append(list(i)+[-sum(i)])
    # print(minus)
    # print(plus)
    return res


print(three_sum([-1, 0, 1, 2, -1, -4]))
# [[0, 1, -1], [-1, -1, 2]]