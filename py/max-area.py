def max_area(height):
    """
    :type height: List[int]
    :rtype: int
    """
    res, i, j = 0, 0, len(height) - 1
    while i < j:
        h = min(height[i], height[j])
        res = max(res, h * (j - i))
        while h == height[i]:
            i += 1
        while h == height[j]:
            j -= 1
    return res


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# 49