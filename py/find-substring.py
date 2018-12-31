from itertools import permutations
from functools import reduce


def find_substring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    res = []
    for i in permutations(words):
        res += index(s, reduce(lambda x, y: x + y, i))
    return res


def index(s, p):
    count = 0
    res = []
    while p in s[count:]:
        index_ = count+s[count:].index(p)
        res.append(index_)
        count = index_+len(p)
    return res


print(find_substring('barfoothefoobarman', ["foo", "bar"]))
print(find_substring('wordgoodstudentgoodword', ["word", "student"]))
# [9, 0]
# []