import math


def smallestGoodBase(n):
    """
    :type n: str
    :rtype: str
    """
    # 过滤
    if n.startswith('0') or not n.isdigit():
        return '"请输入有效且没有前导 0。"'
    num = int(n)

    # 判断二进制是否成功
    if '0' not in bin(num)[2:]:
        return '"2"'

    max_n = int(math.log(num, 2))

    for n in range(max_n, 2, -1):
        # num 的 1 / (n - 1) 次方，且 num 为整数
        x = int(num ** ((n - 1) ** -1))
        # 等比数列求和公式
        if (x ** n - 1) // (x - 1) == num:
            return f'"{str(x)}"'

    # n = 1 时, x = num − 1 且为最大可行解
    return f'"{str(num - 1)}"'


print(smallestGoodBase('13'))
print(smallestGoodBase('8'))
print(smallestGoodBase('4681'))
print(smallestGoodBase('1000000000000000000'))

# "3"
# "7"
# "8"
# "999999999999999999"