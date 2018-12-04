from itertools import combinations


def largestTriangleArea(points):
    """
    :type points: List[List[int]]
    :rtype: float
    """
    return max([s(i) for i in combinations(points, 3)])


def s(points):
    """
    叉乘
    |a×b| = |a||b|sin(θ) = |a1xb2 - a2xb1|
    s = a×h = a×b×sin(θ)/2 = |a1xb2 - a2xb1|/2
    (a1a2)，(x2,y2)
    :param points: List[List[int]]
    :return: float
    """
    a = [points[0][0] - points[1][0], points[0][1] - points[1][1]]
    b = [points[0][0] - points[2][0], points[0][1] - points[2][1]]
    return abs(a[0] * b[1] - a[1] * b[0]) / 2


print(largestTriangleArea([[0, 0], [0, 2], [2, 0]]))
print(largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
# 2.0
# 2.0