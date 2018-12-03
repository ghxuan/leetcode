
import random


class Solution:

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        x = round(2 * (random.random() - 0.5) * self.r + self.x, 5)
        y = round(2 * (random.random() - 0.5) * (self.r ** 2 - (x - self.x) ** 2) ** 0.5 + self.y, 5)
        # return (x-self.x) ** 2 + (y-self.y) ** 2 <= self.r ** 2
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()


obj = Solution(1, 0, 0)
param_1 = obj.randPoint()
print(param_1)

obj = Solution(10, 5, -7.5)
param_2 = obj.randPoint()
print(param_2)

res = [obj.randPoint() for i in range(10000)]
print(all([True if (point[0] - obj.x) ** 2 + (point[1] - obj.y) ** 2 <= obj.r ** 2 else False for point in res]))
# [-0.88721, -0.02666]
# [5.64713, -0.58216]
# True
