from functools import reduce


def fractionAddition(expression):
    """
    :type expression: str
    :rtype: str
    """
    # 将所有的数提取出来
    res = [int(f'-{j}') if expression[i - 1] == '-' else int(j) for i, j in enumerate(expression) if j not in '-+/']
    # 求分母
    denominator = reduce(lambda x, y: x * y, set([i for i in res[1::2]]))
    # 求分子
    numerator = sum([j * denominator // res[i * 2 + 1] for i, j in enumerate(res[0:-1:2])])
    # 求最小公约数
    temp = gcd(numerator, denominator)
    # 返回
    return f'{numerator//temp} / {denominator//temp}'


def gcd(a, b):
    return gcd(b, a % b) if b else a


print(fractionAddition("-1/2+1/2"))
print(fractionAddition("-1/2+1/2+1/3"))
print(fractionAddition("1/3-1/2"))
print(fractionAddition("5/3+1/3"))
# 0 / 1
# 1 / 3
# -1 / 6
# 2 / 1