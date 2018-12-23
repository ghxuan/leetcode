def max_area(height):
    """
    :type height: List[int]
    :rtype: int
    """
    res, i, j = 0, 0, len(height) - 1
    while i < j:
        # h = min(height[i], height[j])
        # area = h * (j - i)
        # if area > res:
        #     res = area
        # while h >= height[i] and i < j:
        #     i += 1
        # while h >= height[j] and i < j:
        #     j -= 1

        if height[i] < height[j]:
            area = height[i] * (j - i)
            i += 1
        else:
            area = height[j] * (j - i)
            j -= 1
        if area > res: 
            res = area
    return res


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_area([1, 1]))
# 49
# 1