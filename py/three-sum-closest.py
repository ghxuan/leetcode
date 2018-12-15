from itertools import combinations


def three_sum_closest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    return sum(sorted(combinations(nums, 3), key=lambda x: abs(sum(x) - target))[0])


print(three_sum_closest([-1, 2, 1, -4], 1))
print(three_sum_closest([-1, 4, 1, -4], 1))
# 2
# 1