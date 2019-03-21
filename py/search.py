def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


print(search([4, 5, 6, 7, 0, 1, 2], target=0))
print(search([4, 5, 6, 7, 0, 1, 2], target=3))

# 4
# -1