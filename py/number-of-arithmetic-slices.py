def number_of_arithmetic_slices(a):
    """
    :type a: List[int]
    :rtype: int
    """
    res = cur = 0
    for i, j in enumerate(a[1:-1]):
        # 假如说 从 P 到 Q 是等差数列
        # P-Q == 2  res=1
        # P-Q > 2   res=1+2+···+(P-Q-1)
        # j-a[i] == a[i+2]-j 说明发现 cur+1 个等差数列 长度分别为 3、4、···、cur+3
        if j-a[i] == a[i+2]-j:
            cur += 1
            res += cur
        else:
            cur = 0
    return res


print(number_of_arithmetic_slices([1, 2, 3, 4]))
print(number_of_arithmetic_slices([1, 2, 3, 4, 5]))
print(number_of_arithmetic_slices([1, 2, 3, 4, 7, 1, 2, 3, 4]))
# 3
# 6
# 6