def search_range(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    res, n = [-1, -1], len(nums)
    if not nums:
        return res
    left, right = 0, n - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[right] != target:
        return res
    res[0], right = right, n
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    res[1] = left - 1
    return res


# def search_range(nums, target):
#     idx = search(nums, 0, len(nums) - 1, target)
#     if idx == -1: return [-1, -1]
#     left = right = idx
#     while left > 0 and nums[left - 1] == nums[idx]: left -= 1
#     while right < len(nums) - 1 and nums[right + 1] == nums[idx]:  right += 1
#     return [left, right]
#
#
# def search(nums, left, right, target):
#     if left > right: return -1
#     mid = left + (right - left) // 2
#     if nums[mid] == target: return mid
#     elif nums[mid] < target: return search(nums, mid + 1, right, target)
#     else: return search(nums, left, mid - 1, target)

print(search_range([5, 7, 7, 8, 8, 10], 8))
print(search_range([5, 7, 7, 8, 8, 10], 6))
print(search_range([8, 8] * 3, 8))

# [3, 4]
# [-1, -1]
# [0, 5]