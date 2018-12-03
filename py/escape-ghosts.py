
def escapeGhosts(ghosts, target):
    """
    :type ghosts: List[List[int]]
    :type target: List[int]
    :rtype: bool
    """
    # 敌人到终点的最小距离
    min_ = min([abs(i[0]-target[0])+abs(i[1]-target[1]) for i in ghosts])
    you = abs(target[0])+abs(target[1])
    if you < min_:
        return True
    return False


print(escapeGhosts([[1, 0], [0, 3]], [0, 1]))
print(escapeGhosts([[1, 0]], [2, 0]))
print(escapeGhosts([[2, 0]], [1, 0]))
# True
# False
# False
