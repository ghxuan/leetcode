def count_and_say(n):
    """
    :type n: int
    :rtype: str
    """

    if n == 1:
        return '1'
    return read(count_and_say(n - 1))


def read(n):
    last, res, count = n[0], '', 0
    for m in n:
        if last == m:
            count += 1
        else:
            res += str(count) + last
            count = 1
            last = m
    res += (str(count) + last) if count else res
    return res


print(count_and_say(1))
print(count_and_say(2))
print(count_and_say(3))
print(count_and_say(4))
print(count_and_say(5))
print(count_and_say(6))

# 1
# 11
# 21
# 1211
# 111221
# 312211