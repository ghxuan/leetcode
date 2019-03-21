def search_insert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums:
        return 0
    left, right, mid = 0, len(nums) - 1, 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    if nums[mid] >= target:
        return mid
    else:
        return mid + 1

    # if not nums:
    #     return 0
    # if nums[-1] < target:
    #     return len(nums)
    # left, right = 0, len(nums) - 1
    # while left < right:
    #     mid = (right + left) // 2
    #     if nums[mid] == target:
    #         return mid
    #     elif nums[mid] < target:
    #         left = mid + 1
    #     else:
    #         right = mid
    # return right


print(search_insert([1, 3, 5, 6], 4))
print(search_insert([1, 3, 5, 6], 7))

# 2
# 4