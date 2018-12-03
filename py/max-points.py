
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
from itertools import combinations


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
        if b:
            self.k = a/b
        else:
            self.k = None

    def __repr__(self):
        return f'[{self.x}, {self.y}]'

    def __eq__(self, other):
        return self.k == other.k

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        res = combinations(points, 2)
        res_list = [i-j for i, j in res]
        # 排列组合
        # max_ 最小为 C22 结果肯定为整数
        all_ = {}
        for i in res_list:
            if i.k in all_:
                all_[i.k] += 1
            else:
                all_[i.k] = 1
        # C42 = 4*3*0.5 = max_
        # n^2 - n - 2*max_ = 0
        # res = (-b +- (b^2- 4(-2*max_))**0.5)*0.5
        # res > 0
        # return (-b + (b^2- 4(-2*max_))**0.5)*0.5
        # res(.0) 不好看 int()
        return int((1+(1+4*2*max(all_.values()))**0.5)*0.5)


s = Solution()
print(s.maxPoints([Point(i, j) for i, j in [[1, 1], [2, 2], [3, 3]]]))
print(s.maxPoints([Point(i, j) for i, j in [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]]))
# 3
# 4
