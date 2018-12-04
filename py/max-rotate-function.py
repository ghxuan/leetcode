def maxRotateFunction(A):
    """
    :type A: List[int]
    :rtype: int
    """
    length = len(A)
    sum_a = sum(A)
    f = 0
    last_f = sum([i * A[i] for i in range(length)])
    for i in range(1, length):
        last_f = last_f + sum_a - length * A[-i]
        if last_f > f:
            f = last_f
    return f


print(maxRotateFunction([4, 3, 2, 6]))
print(maxRotateFunction([i for i in range(100000)]))
# 26
# 333323333400000