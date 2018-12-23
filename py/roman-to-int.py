def roman_to_int(s):
    """
    :type s: str
    :rtype: int
    """
    dict_ = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    res, temp = 0, 0
    for string in s[::-1]:
        cur = dict_[string]
        res, temp = res - cur if cur < temp else res + cur, cur
    return res


print(roman_to_int('III'))
print(roman_to_int('IV'))
print(roman_to_int('IX'))
print(roman_to_int('LVIII'))
print(roman_to_int('MCMXCIV'))
# 3
# 4
# 9
# 58
# 1994