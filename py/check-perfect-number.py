def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    return not (sum(
        [sum({i, divmod(num, i)[0]})
         for i in range(2, int(num ** 0.5) + 1)
         if not divmod(num, i)[1]]
    ) + 1 - num if num != 1 else 1)


print(checkPerfectNumber(28))
# True