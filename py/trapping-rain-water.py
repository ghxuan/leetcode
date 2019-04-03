def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    low = res = 0
    hei = len(height) - 1
    while low < hei:
        mn = min(height[low], height[hei])
        if mn == height[low]:
            low += 1
            while low < hei and height[low] < mn:
                res += mn - height[low]
                low += 1
        else:
            hei -= 1
            while low < hei and height[hei] < mn:
                res += mn - height[hei]
                hei -= 1
    return res


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6