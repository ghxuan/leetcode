def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    num = str.strip(' ')
    if len(num) == 0:
        return 0
    temp = '-+123456789'
    if (num[0] in temp[:2] and num[1] != '0') or num[0] in temp[2:]:
        temp = temp[2:] + '0'
        for i in range(1, len(num)):
            if num[i] not in temp:
                num = num[:i]
                break
        num = int(num)
        if num < -2147483648:
            return -2147483648
        elif num > 2147483647:
            return 2147483647
        return num
    return 0


print(myAtoi('42'))
print(myAtoi('   -042'))
print(myAtoi('4193 with words'))
print(myAtoi('words and 987'))
print(myAtoi('-91283472332'))
print(myAtoi(''))

# 42
# 0
# 4193
# 0
# -2147483648
# 0