def three_sum_closest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # nums.sort()
    # res, n = sum(nums[:3]), len(nums)
    # diff = abs(target - res)
    # for index, num in enumerate(nums[:-2]):
    #     left, right = index + 1, n - 1
    #     while left < right:
    #         three_sum = num + nums[left] + nums[right]
    #         new_diff = target - three_sum
    #         if new_diff < 0:
    #             new_diff = -new_diff
    #             right -= 1
    #         else:
    #             left += 1
    #         if new_diff < diff:
    #             diff = new_diff
    #             res = three_sum
    # return res

    nums.sort()
    res, n = [], len(nums)
    for index, num in enumerate(nums[:-2]):
        left, right = index + 1, n - 1
        if num + nums[left] + nums[left + 1] > target:
            res.append(num + nums[left] + nums[left + 1])
            break
        elif num + nums[right] + nums[right - 1] < target:
            res.append(num + nums[right] + nums[right - 1])
        else:
            while left < right:
                temp = num + nums[left] + nums[right]
                res.append(temp)
                if temp > target:
                    right -= 1
                elif temp < target:
                    left += 1
                else:
                    return target
    res.sort(key=lambda x: abs(x - target))
    return res[0]


print(three_sum_closest([-1, 2, 1, -4], 1))
print(three_sum_closest([-1, 4, 1, -4], 1))
# 2
# 1