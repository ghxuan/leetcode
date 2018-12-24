def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    dict_ = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }
    res, n1, n2 = 0, 0, 0
    # for n, i in enumerate(num1[::-1]):
    #     for m, j in enumerate(num2[::-1]):
    #         res += dict_[i] * dict_[j] * 10 ** (m + n)
    # return str(res)
    for i in num1:
        n1 = dict_[i] + n1 * 10
    for j in num2:
        n2 = dict_[j] + n2 * 10
    return str(n1 * n2)


print(multiply('1', '1'), 1)
print(multiply('12', '12'), 12 * 12)
print(multiply('156', '156'), 156 * 156)
print(multiply("123", "456"), 123 * 456)
# 1 1
# 144 144
# 24336 24336
# 56088 56088