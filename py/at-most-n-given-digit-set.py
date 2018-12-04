from functools import reduce


def at_most_n_given_digit_set(d, n):
    """
    :type d: List[str]
    :type n: int
    :rtype: int
    """
    if '0' in d or any([len(i) != 1 for i in d]):
        return 0

    # match 为当前数字有几个小于本身的数在 d 列表中(不包括本身)
    match = {}
    e = 0
    for i in '123456789':
        match[i] = e
        if i in d:
            e += 1

    str_n = str(n)
    len_ = len(str_n)
    len_d = len(d)
    index = len_
    for i, j in enumerate(str_n[1:]):
        if j not in d:
            # 第一个除了首位的 未知数 的位置
            index = i+1
            break

    # 首先，看下面第一部分 len_ 位数肯定大于 len_-1 位数
    # [len_d ** i for i in range(1, len_)]
    # 然后，看再下面第二部分，str_n 里面不能有不在 d 中的数 ，遇到 未知数 就只能保证之前的都小于 n 了，
    # 例如：[1,2,3] 202 因为 d 里面没有 0 ，所以 201、202 肯定不成立，只有 1[1,2,3][1,2,3], 将 0 换成其它数也一样

    # 因为 match 不包括其本身，所以假如
    # n 里面的所有数都在 d 里面的话，返回的数不包含其本身 n
    # print([match[str_n[j]] * (len_d ** (len_ - 1 - j)) for j in range(index)])
    res = 1 if index == len_ and str_n[-1] in d else 0
    return sum([len_d ** i for i in range(1, len_)] +
               [match[str_n[j]] * (len_d ** (len_ - 1 - j)) for j in range(index)])+res


def same(d, n):
    """
    :type d: List[str]
    :type n: int
    :rtype: int
    """
    d = set(d)
    res = 0
    for i in range(n+1):
        if all([i in d for i in set(str(i))]):
            # print(i)
            res += 1
    return res


print(at_most_n_given_digit_set(["1", "3", "5", "7"], 110), same(["1", "3", "5", "7"], 110))
print(at_most_n_given_digit_set(["1", '2', "3", "5", "7"], 202), same(["1", '2', "3", "5", "7"], 202))
print(at_most_n_given_digit_set(["1", "3", "5", "7"], 222), same(["1", "3", "5", "7"], 222))
print(at_most_n_given_digit_set(["1", '2', "3", "5", "7"], 222), same(["1", '2', "3", "5", "7"], 222))
print(at_most_n_given_digit_set(["1", "3", "5", "7", '9'], 999), same(["1", "3", "5", "7", '9'], 999))
# 20 20
# 55 55
# 36 36
# 62 62
# 155 155