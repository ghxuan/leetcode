def four_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    # nums.sort()
    # res, n = set(), len(nums)
    # dict_ = dict((tuple(nums[start:start + 4]), sum(nums[start:start + 4]) - target)
    #              for start, _ in enumerate(nums[:-3]))
    # for start, num1 in enumerate(nums[:-3]):
    #     for end, num2 in enumerate(nums[start + 3::]):
    #         cur = start + end
    #         left, right = start + 1, cur + 2
    #         if dict_[tuple(nums[start:start + 4])] <= 0 <= dict_[tuple(nums[cur:cur + 4])]:
    #             while left < right:
    #                 temp = (num1, nums[left], nums[right], num2)
    #                 dict_[temp] = diff = dict_.get(temp, sum(temp) - target)
    #                 if diff > 0:
    #                     right -= 1
    #                 elif diff < 0:
    #                     left += 1
    #                 else:
    #                     res.add(temp)
    #                     right -= 1
    # return [list(i) for i in res]

    nums.sort()
    res, n = [], len(nums)
    for first, num1 in enumerate(nums[:-3]):
        target1 = target - num1
        if sum(nums[first:first + 4]) > target:
            break
        elif sum(nums[-3:]) < target1 or (first > 0 and num1 == nums[first - 1]):
            continue
        for second in range(first + 1, n - 2):
            target2 = target1 - nums[second]
            if nums[second + 1] + nums[second + 2] > target2:
                break
            elif nums[-2] + nums[-1] < target2 or (second > first + 1 and nums[second] == nums[second - 1]):
                continue
            left, right = second + 1, n - 1
            while left < right:
                temp = nums[left] + nums[right]
                if temp > target2:
                    right -= 1
                elif temp < target2:
                    left += 1
                else:
                    res.append([num1, nums[second], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left, right = left + 1, right - 1
    return res


print(four_sum([1, 0, -1, 0, -2, 2], 0))
print(four_sum([-1, -5, -5, -3, 2, 5, 0, 4], -7))
# [[1, 0, -1, 0], [1, -1, -2, 2], [0, 0, -2, 2]]
# [[-5, -5, -1, 4], [-5, -3, -1, 2]]