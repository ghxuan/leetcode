def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    res, minus, plus, count = [], [], [], {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if num < 0:
            minus.append(num)
        else:
            plus.append(num)
    m, p = set(minus), set(plus)

    if 0 in count and count[0] >= 3:
        res.append([0, 0, 0])
    for i in m:
        for j in p:
            temp = -i - j
            if temp in count and (temp < i or temp > j or (temp in {i, j} and count[temp] > 1)):
                res.append([i, j, temp])
    return res


print(three_sum([-1, 0, 1, 2, -1, -4]))
# [[0, 1, -1], [-1, -1, 2]]