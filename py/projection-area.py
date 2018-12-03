
def projectionArea(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    xy = yz = xz = 0
    yz_temp = [0 for _ in grid]
    for i in grid:
        xz += max(i)
        for m, j in enumerate(i):
            if j:
                xy += 1
                if j > yz_temp[m]:
                    yz_temp[m] = j
    yz = yz + sum(yz_temp)
    return xy + xz + yz


print(projectionArea([[2]]))
print(projectionArea([[1, 2], [3, 4]]))
print(projectionArea([[1, 0], [0, 2]]))
print(projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
# 5
# 17
# 8
# 14
# 21
