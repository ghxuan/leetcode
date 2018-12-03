
def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    int_dict = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    res = ''
    keys = list(int_dict.keys())[::-1]
    values = list(int_dict.values())[::-1]
    for i, j in enumerate(keys):
        while num >= j:
            temp = num // j
            num -= j * temp
            res += values[i] * temp
    return res


print(intToRoman(3))
print(intToRoman(4))
print(intToRoman(9))
print(intToRoman(58))
print(intToRoman(1994))
# III
# IV
# IX
# LVIII
# MCMXCIV
