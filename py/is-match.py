def is_match(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    left, right = count(s), count(p)
    # print(left, right)
    index = 0
    p, q = 0, 0
    for i in left:
        m, n = i.popitem()
        if not q.imag:
            p, q = right[index].popitem()
        # print(m, n, p, q)
        if m == p or p == '.':
            if q.imag:
                if q.real - 1 > n:
                    return False
            elif q.real < n:
                return False
            else:
                index += 1
        elif q.imag:
            q = 0
            index += 1
        else:
            return False
    return True


def count(s):
    next_ = ''
    list_ = []
    for i in s:
        if i == next_:
            list_[len(list_) - 1][i] += 1
        elif i == '*':
            list_[len(list_) - 1][next_] += 1j
        else:
            list_.append({i: 1})
            next_ = i
    return list_


print(is_match('aa', 'a'))
print(is_match('aa', 'a*'))
print(is_match('ab', '.*'))
print(is_match('aab', 'c*a*b'))
print(is_match('mississippi', 'miss*is*p*.'))
print(is_match('', ''))
# False
# True
# True
# True
# False
# True