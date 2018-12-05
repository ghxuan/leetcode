def add_binary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    res = ''
    a1 = len(a)
    b1 = len(b)
    m = max(a1, b1)
    temp = 0
    for i in range(m):
        aa = int(a[-i - 1]) if i < a1 else 0
        bb = int(b[-i - 1]) if i < b1 else 0
        temp, num = divmod(aa+bb+temp, 2)
        res = str(num)+res
    return '1'+res if temp else res


print(add_binary('11', '1'))
print(add_binary('1010', '1011'))
# 100
# 10101