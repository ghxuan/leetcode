def int_to_roman(num):
    """
    :type num: int
    :rtype: str
    """
    # dict_ = {
    #     1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
    #     90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
    #     9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    # }
    # res = ''
    # for key, value in dict_.items():
    #     if num >= key:
    #         temp, num = divmod(num, key)
    #         res += value * temp
    # return res

    list_ = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
        (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    res = ''
    for key, value in list_:
        while num >= key:
            num -= key
            res += value
    return res


print(int_to_roman(3))
print(int_to_roman(4))
print(int_to_roman(9))
print(int_to_roman(58))
print(int_to_roman(1994))
# III
# IV
# IX
# LVIII
# MCMXCIV