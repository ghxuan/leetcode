from functools import reduce


def convert(s, num_rows):
    """
    :type s: str
    :type num_rows: int
    :rtype: str
    """
    new = [''] * num_rows
    temp = 0
    # 因为无论如何第一次 not temp 的时候肯定会判断，
    # 然而后面需要是递增的，
    # 所以 add 初始值为 -1
    add = -1
    for j in s:
        new[temp] += j
        # 每到一次头就要转一次向
        if not temp or temp == num_rows - 1:
            add *= -1
        temp += add
    return reduce(lambda x, y: x + y, new)


print(convert('LEETCODEISHIRING', 3))
print(convert('LEETCODEISHIRING', 4))
print(convert('LEETCODEISHIRING', 5))
# LCIRETOESIIGEDHN
# LDREOEIIECIHNTSG
# LIEESGEDHNTOIICR