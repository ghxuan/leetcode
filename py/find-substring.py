def find_substring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    length = dict((word, len(word)) for word in words)
    lens, lenw, lenws = len(s), len(words[0]), len(words)
    longest, temp, left, cur, res = lens - lenw + 1, [False] * lenws, 0, 0, []
    while cur < longest:
        string = s[cur:cur + lenw]
        if string in length:
            temp[left] = [cur]
            left += 1
            if all(temp):
                res.append(temp[0][0])
            cur += lenw
        else:
            left, temp = 0, [False] * lenws
            cur += 1
    return res

    
# from itertools import permutations
# from functools import reduce
# def find_substring(s, words):
#     """
#     :type s: str
#     :type words: List[str]
#     :rtype: List[int]
#     """
#     res = []
#     for i in permutations(words):
#         res += index(s, reduce(lambda x, y: x + y, i))
#     return res


# def index(s, p):
#     count = 0
#     res = []
#     while p in s[count:]:
#         index_ = count+s[count:].index(p)
#         res.append(index_)
#         count = index_+len(p)
#     return res


print(find_substring('barfoothefoobarman', ["foo", "bar"]))
print(find_substring('wordgoodstudentgoodword', ["word", "student"]))
# [9, 0]
# []