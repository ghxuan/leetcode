import re


def my_atoi(string):
    """
    :type string: str
    :rtype: int
    """
    # num = string.strip(' ')
    # temp, n = '+-0123456789', len(num)
    # if n > 0 and num[0] in temp:
    #     temp = temp[2:]
    #     for i in range(1, n):
    #         if num[i] not in temp:
    #             num = num[:i]
    #             break
    #     num = 0 if len(num) == 1 and num[0] in '-+' or ('+' in num and '-' in num) else int(num.replace('+', ''))
    #     if num < -2147483648:
    #         return -2147483648
    #     elif num > 2147483647:
    #         return 2147483647
    #     return num
    # return 0

    string = string.strip()
    try:
        res = int(re.search('^[+-]?\d+', string).group())
        res = res if res <= 2147483647 else 2147483647
        res = res if res >= -2147483648 else -2147483648
    except:
        return 0
    return res


print(my_atoi('42'))
print(my_atoi('   -042'))
print(my_atoi('4193 with words'))
print(my_atoi('words and 987'))
print(my_atoi('-91283472332'))
print(my_atoi(''))
print(my_atoi("  0000000000012345678"))
print(my_atoi('-'))
# 42
# -42
# 4193
# 0
# -2147483648
# 0
# 12345678
# 0