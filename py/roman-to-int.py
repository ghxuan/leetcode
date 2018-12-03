
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    int_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    sum_s = 0
    for i in range(len(s)):
        sum_s += int_dict[s[i]]
        if int_dict[s[i]] > int_dict[s[i-1]]:
            sum_s -= 2*int_dict[s[i-1]]
    return sum_s


print(romanToInt('III'))
print(romanToInt('IV'))
print(romanToInt('IX'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))
# 3
# 4
# 9
# 56
# 1984
