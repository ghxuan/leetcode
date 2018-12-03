
def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    len_ = len(nums)
    temp = sorted(nums)
    res = [[] for _ in temp]
    for n, i in enumerate(temp):
        for m, j in enumerate(temp[::-1]):
            if i % j == 0:
                if not res[n]:
                    res[n].append(j)
                else:
                    res[n] += res[len_-m-1]
                    break
    max_ = 0
    result = []
    for i in res:
        if len(i) > max_:
            max_ = len(i)
            result = i
    return result


print(largestDivisibleSubset([1, 2, 3, 4, 5, 6]))
print(largestDivisibleSubset([1, 2, 4, 8]))
print(largestDivisibleSubset([2, 3, 4, 8, 9, 27]))
# [4, 2, 1]
# [8, 4, 2, 1]
# [8, 4, 2]
