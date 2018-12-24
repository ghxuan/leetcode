def generate_parenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    # res = []
    #
    # def generate(left, right, out=''):
    #     if right < left:
    #         return
    #     if right == left == 0:
    #         res.append(out)
    #     if left > 0:
    #         generate(left - 1, right, out + '(')
    #     if right > 0:
    #         generate(left, right - 1, out + ')')
    #
    # generate(n, n)
    # return res

    dp = {0: [''], 1: ['()']}
    if n not in dp:
        for i in range(2, n + 1):
            # for m in range(i):
            #     for sl in dp[m]:
            #         for sr in dp[i - m - 1]:
            #             print('(' + sl + ')' + sr, m, i-m-1)
            dp[i] = ['(' + sl + ')' + sr for m in range(i) for sl in dp[m] for sr in dp[i - m - 1]]
    return dp[n]


print(generate_parenthesis(3))
# ['()(())', '((()))', '(())()', '(()())', '()()()']