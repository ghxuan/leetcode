
def add_strings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    number = {str(i): i for i in range(10)}
    m1 = len(num1)
    m2 = len(num2)
    m = max(m1, m2)
    res = ''
    temp = 0
    for i in range(m):
        n1 = num1[-i-1] if i < m1 else '0'
        n2 = num2[-i-1] if i < m2 else '0'
        temp, num = divmod(number[n1]+number[n2]+temp, 10)
        res = str(num)+res
    return '1'+res if temp else res


print(add_strings('5000', '5000'))
print(add_strings('4321', '1234'))
print(add_strings('1234', '8888'))
print(add_strings('1234', '321'))
# 10000
# 5555
# 10122
# 1555
