

def surfaceArea(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    res = 0
    len_i = len(grid)
    len_j = len(grid[0])
    for i in range(len_i):
        for j in range(len_j):
            res += grid[i][j] * 4 + 2
            try:
                temp = min(grid[i][j], grid[i][j + 1])
                res -= temp * 2
            except:
                pass
            try:
                temp = min(grid[i][j], grid[i + 1][j])
                res -= temp * 2
            except:
                pass
    return res


print(surfaceArea([[2]]))
print(surfaceArea([[1, 2], [3, 4]]))
print(surfaceArea([[1, 0], [0, 2]]))
print(surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))

# 10
# 34
# 20
# 34
# 46

