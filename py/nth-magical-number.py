def nthMagicalNumber(n, a, b):
    """
    :type n: int
    :type a: int
    :type b: int
    :rtype: int
    """
    temp = lcm(a, b)
    temp_a = temp//b
    temp_b = temp//a
    for_list = [0]+sorted([a*i for i in range(1, temp_a+1)]+[b*i for i in range(1, temp_b+1)])[:-1]
    a, b = divmod(n, len(for_list)-1)
    return a*temp+for_list[b]


def gcd(a, b):
    return gcd(b, a % b) if b else a


def lcm(a, b):
    return a * b // gcd(a, b)


print(nthMagicalNumber(1, 2, 3))
print(nthMagicalNumber(4, 2, 3))
print(nthMagicalNumber(5, 2, 4))
print(nthMagicalNumber(3, 6, 4))
# 2
# 6
# 10
# 8