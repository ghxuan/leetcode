def solveEquation(equation):
    """
    :type equation: str
    :rtype: str
    """
    left, right = equation.split('=')

    # 这个列表推导式可以分为两部分：
    # 1、去除 '+' 号：if '-' in i else i for i in left.split('+')
    # 2、去除 '-' 号
    left_ = [j if j == i.split('-')[0] else '-' + j if '-' in i else i for i in left.split('+') for j in i.split('-')]
    right_ = [j if j == i.split('-')[0] else '-' + j if '-' in i else i for i in right.split('+') for j in i.split('-')]

    left_ = left_ + [i[1:] if '-' in i else '-' + i for i in right_]

    # 左为x，右为数
    left, right = list(zip(*[[i[:-1], '0'] if 'x' in i else ['0', i] for i in left_]))

    def num_filter(num_list):
        n = []
        for num in num_list:
            if num == '':
                n.append(1)
            elif '-' in num and len(num) == 1:
                n.append(-1)
            elif num != '0':
                n.append(int(num))
        return sum(n)

    left = num_filter(left)
    right = num_filter(right)*-1
    if not left:
        if not right:
            return 'Infinite solutions'
        return 'No solution'
    return f'x={int(right/left)}'


print(solveEquation('x+5-3+x=6+x-2'))
print(solveEquation('x=x'))
print(solveEquation('2x=x'))
print(solveEquation('2x+3x-6x=x+2'))
print(solveEquation('x=x+2'))


# x=2
# Infinite solutions
# x=0
# x=-1
# No solution