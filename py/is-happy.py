def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    last = [n]
    while n != 1:
        n = sum([int(i)**2 for i in str(n)])
        if n in last:
            return False
        last.append(n)
    return True


print(isHappy(19))
# True