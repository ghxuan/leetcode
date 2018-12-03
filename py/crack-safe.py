
def crackSafe(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    res = '0' * n
    temp = res[1 - n:]
    length = k ** n
    res_set = {res}
    while len(res_set) < length:
        for i in range(k - 1, -1, -1):
            num = str(i)
            if temp + num in res_set:
                continue
            res += num
            temp = res[1 - n:]
            res_set.add(res[-n:])
            break
    # print(res_set, len(res_set))
    return res


print(crackSafe(1, 2))
print(crackSafe(2, 2))
print(crackSafe(4, 2))
# 01
# 00110
# 0000111101100101000
