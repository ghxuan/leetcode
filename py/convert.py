def convert(s, num_rows):
    """
    :type s: str
    :type num_rows: int
    :rtype: str
    """
    if num_rows == 1 or num_rows >= len(s):
        return s
    res = [''] * num_rows
    temp, add, cur = 0, 0, num_rows - 1
    for sting in s:
        res[temp] += sting
        # 每到一次头就要转一次向
        if temp == 0:
            add = 1
        elif temp == cur:
            add = -1
        temp += add
    return ''.join(res)


print(convert('LEETCODEISHIRING', 3))
print(convert('LEETCODEISHIRING', 4))
print(convert('LEETCODEISHIRING', 5))
# LCIRETOESIIGEDHN
# LDREOEIIECIHNTSG
# LIEESGEDHNTOIICR