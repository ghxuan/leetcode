
def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    res = 0
    for n, i in enumerate(num1[::-1]):
        for m, j in enumerate(num2[::-1]):
            res += int(i)*int(j)*10**(m+n)
    return str(res)


print(multiply('1', '1'), 1)
print(multiply('12', '12'), 12*12)
print(multiply('156', '156'), 156*156)
# 1 1
# 144 144
# 24336 24336
