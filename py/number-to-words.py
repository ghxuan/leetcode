import math


def numberToWords(num):
    """
    :type num: int
    :rtype: str
    """
    english = {
        '1': 'One', '2': 'Two', '3': 'Three',
        '4': 'Four', '5': 'Five', '6': 'Six',
        '7': 'Seven', '8': 'Eight', '9': 'Nine',
        '10': 'Ten', '11': 'Eleven', '12': 'Twelve',
        '13': 'Thirteen', '14': 'Fourteen', '15': 'Fifteen',
        '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen',
        '19': 'Nineteen', '20': 'Twenty', '30': 'Thirty',
        '40': 'Forty', '50': 'Fifty', '60': 'Sixty',
        '70': 'Seventy', '80': 'Eighty', '90': 'Ninety'
    }
    count_zero = ['Hundred', 'Thousand', 'Million', 'Billion']
    res = ''
    num = str(num)[::-1]
    for i in range(0, math.ceil(len(num) / 3)):
        if 0 < i <= 3:
            res = ' ' + count_zero[i] + ' ' + res
        temp = num[i * 3:i * 3 + 3][::-1]
        if temp[-2:] in english:
            res = english[temp[-2:]] + res
        else:
            res = english[temp[-2] + '0'] + ' ' + english[temp[-1]] + res
        if len(temp) == 3:
            res = english[temp[0]] + ' ' + count_zero[0] + ' ' + res
    return res


print(numberToWords(123))
print(numberToWords(12345))
print(numberToWords(1234567))
print(numberToWords(1234567891))
# One Hundred Twenty Three
# Twelve Thousand Three Hundred Forty Five
# One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven
# One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One