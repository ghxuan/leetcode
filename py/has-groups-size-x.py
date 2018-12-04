def hasGroupsSizeX(deck):
    """
    :type deck: List[int]
    :rtype: bool
    """
    temp = tuple(set([deck.count(i) for i in set(deck)]))
    min_ = min(temp)
    res = all([0 if i % min_ else 1 for i in temp])
    return res if min_ >= 2 else False
    # PEP572 写法
    # return all(
    # [0 if i % min_:=tuple(temp) else 1
    # for i in temp:=set(
    # [deck.count(i) for i in set(deck)])])
    # if min_ >= 2 else False


print(hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
print(hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
print(hasGroupsSizeX([1]))
print(hasGroupsSizeX([1, 1]))
print(hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
# True
# False
# False
# True
# True