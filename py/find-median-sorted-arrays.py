def find_median_sorted_arrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m1 = len(nums1)
    m2 = len(nums2)
    # (m1 + m2 + 1) // 2)
    # (m1 + m2 + 2) // 2)
    # 当 m1+m2 是奇数时，上面两数相等，正好是中间的一个数的索引
    # 当 m1+m2 是偶数时，上面两数不等，正好是中间的两个数的索引
    a = (m1 + m2 + 1) // 2
    b = (m1 + m2 + 2) // 2
    if a == b:
        return find(nums1, nums2, a)
    return (find(nums1, nums2, a) + find(nums1, nums2, b)) / 2.0


def find(nums1, nums2, k):
    if not nums1:
        return nums2[k - 1]
    if not nums2:
        return nums1[k - 1]
    if k == 1:
        return min(nums1[0], nums2[0])
    # 二分
    i = min(len(nums1), k // 2)
    j = min(len(nums2), k // 2)
    # 判断，切片
    if nums1[i - 1] > nums2[j - 1]:
        return find(nums1, nums2[j:], k - j)
    else:
        return find(nums1[i:], nums2, k - i)


def find_median_sorted_arrays2(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nums = nums1 + nums2
    nums.sort()
    temp, cur = divmod(len(nums), 2)
    if cur:
        return nums[temp]
    return (nums[temp - 1] + nums[temp]) / 2.0


print(find_median_sorted_arrays([1, 3], [2]))
print(find_median_sorted_arrays2([1, 3], [2]))
print(find_median_sorted_arrays([1, 2], [3, 4]))
print(find_median_sorted_arrays2([1, 2], [3, 4]))
print(find_median_sorted_arrays([1, 2, 5, 6], [3, 4]))
print(find_median_sorted_arrays2([1, 2, 5, 6], [3, 4]))
print(find_median_sorted_arrays([1, 3, 5, 6], [2, 4, 7, 8]))
print(find_median_sorted_arrays2([1, 3, 5, 6], [2, 4, 7, 8]))
# 2
# 2
# 2.5
# 2.5
# 3.5
# 3.5
# 4.5
# 4.5