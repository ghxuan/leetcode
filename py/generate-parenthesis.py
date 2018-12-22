def generate_parenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    # 当 n 为 1 时 ()
    # 当 n 为 2 时 set((n=1)*3)
    # 当 n 为 3 时 set((n=2)*3)
    # 当 n 为 4 时 set((n=3)*3)
    # 当 n 为 4 时 set((n=5)*3)
    if n == 1:
        return ['()']
    next_ = generate_parenthesis(n-1)
    res = []
    for i in next_:
        res += [f'{i}()', f'({i})', f'(){i}']
    return list(set(res))


print(generate_parenthesis(3))
# ['()(())', '((()))', '(())()', '(()())', '()()()']