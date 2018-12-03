
import math


def numRabbits(answers):
    """
    :type answers: List[int]
    :rtype: int
    """
    return sum([(i + 1) * math.ceil(answers.count(i) / (i + 1)) for i in set(answers)])


print(numRabbits([1, 1, 1, 1, 2]))
print(numRabbits([1, 1, 2]))
print(numRabbits([10, 10, 10]))
print(numRabbits([10 for i in range(12)]))
print(numRabbits([]))
# 7
# 5
# 11
# 22
# 0
