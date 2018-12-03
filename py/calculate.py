
def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.replace(' ', '')
    fix = postfix(s)
    print(fix)
    temp = []
    sign = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x / y,
        '*': lambda x, y: x * y,
        '×': lambda x, y: x * y,
        '%': lambda x, y: x % y,
    }
    while fix:
        i = fix[0]
        fix.pop(0)
        if i not in '+-×*/%':
            temp.append(int(i))
        else:
            b, a = temp.pop(), temp.pop()
            temp.append(sign[i](a, b))
    return temp[0]


def postfix(s):
    """
    字符串转后缀表达式
    :param s: str
    :return: list
    """
    res = []
    temp = []
    # 优先级
    priority = {
        '+': 1, '-': 1, '*': 2,
        '×': 2, '/': 2, '%': 2,
    }
    for i in s:
        if i not in '*×/%+-()':
            res.append(i)
        elif i == ')':
            for j in temp[::-1]:
                if j == '(':
                    temp.pop()
                    break
                res.append(temp.pop())
        else:
            while True:
                # 判断优先级
                if not temp or temp[-1] == '(' or i == '(' or priority[i] > priority[temp[-1]]:
                    temp.append(i)
                    break
                else:
                    res.append(temp.pop())
                    pass
    res += temp[::-1]
    return res


print(calculate('1 + 1'))
print(calculate(' 2-1 + 2 '))
print(calculate('(1+(4+5+2)-3)+(6+8)'))
print(calculate('1+((2-3+2)×4)-5'))
# ['1', '1', '+']
# 2
# ['2', '1', '-', '2', '+']
# 3
# ['1', '4', '5', '+', '2', '+', '+', '3', '-', '6', '8', '+', '+']
# 23
# ['1', '2', '3', '-', '2', '+', '4', '×', '+', '5', '-']
# 0
