from itertools import combinations


def sumSubseqWidths(A):
    """
    :type A: List[int]
    :rtype: int
    """
    res = 0
    count = dict(zip(a, [0 for _ in a]))
    for i in range(2, len(A) + 1):
        x = list(combinations(A, i))
        for j in x:
            res += max(j) - min(j)
            count[max(j)] += 1
            count[min(j)] -= 1
    print(count)
    return res


print(sumSubseqWidths([2, 1, 3]))
print(sumSubseqWidths([2, 1]))

# {1: -1, 2: 1}
# 1
# {1: -3, 2: 0, 3: 3}
# 6
def sumSubseqWidths(A):
    """
    :type A: List[int]
    :rtype: int
    """
    res = 0
    length = len(A)
    temp = 2 ** (length - 1)
    n = 0
    A.sort()
    for i in range(length - 1, 0, -2):
        res += (A[length - 1 - n] - A[n]) * (temp - 2 ** n)
        temp /= 2
        n += 1
    return int(res)


print(sum_sub_seq_widths([1, 2]))
print(sum_sub_seq_widths([1, 2, 3]))
print(sum_sub_seq_widths([1, 2, 3, 4]))
print(sum_sub_seq_widths([1, 2, 3, 4, 5]))
print(sum_sub_seq_widths([1, 2, 3, 4, 5, 6]))
print(sum_sub_seq_widths([1, 2, 3, 4, 5, 6, 7]))
print(sum_sub_seq_widths([1, 2, 3, 4, 5, 6, 7, 8]))
print(sum_sub_seq_widths([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sum_sub_seq_widths([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 1
# 6
# 23
# 72
# 201
# 522
# 1291
# 3084
# 7181