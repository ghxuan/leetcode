def nthUgly(num):
    """
    :type num: int
    :rtype: bool
    """
    # if num == 1:
    #     return True
    res = num
    while res % 2 == 0:
        res /= 2
    while res % 3 == 0:
        res /= 3
    while res % 5 == 0:
        res /= 5
    if res == 1:
        return True
    return False


print(nthUgly(1))
print(nthUgly(32))
print(nthUgly(-2147483648))
print(nthUgly(78732))
print(nthUgly(600))
print(nthUgly(2147483647))

# True
# True
# False
# True
# True
# False