

def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    all_num = [1 for _ in range(n)]
    x = y = z = 0
    i = 1
    while i < n:
        all_num[i] = min(2*all_num[x], 3*all_num[y], 5*all_num[z])
        if all_num[i] == 2*all_num[x]:
            x += 1
        if all_num[i] == 3*all_num[y]:
            y += 1
        if all_num[i] == 5*all_num[z]:
            z += 1
        i += 1
    return all_num[n-1]


print(nthUglyNumber(1))
print(nthUglyNumber(10))
print(nthUglyNumber(50))


