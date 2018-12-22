def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """
    # left, res, temp, cur = -1, 0, 0, False
    # dict_ = {}
    # for index, string in enumerate(s):
    #     if string in dict_ and dict_[string] >= left:
    #         left = dict_[string]
    #         temp = index - left
    #         cur = False
    #     else:
    #         temp += 1
    #         if cur or res < temp:
    #             res = temp
    #             cur = True
    #     dict_[string] = index
    # # print(dict_)
    # return res

    left, res, index = -1, 0, -1
    dict_ = {}
    for index, string in enumerate(s):
        if string in dict_ and dict_[string] >= left:
            res = max(res, index-left-1)
            left = dict_[string]
        dict_[string] = index
    res = max(res, index - left)
    # print(dict_)
    return res


print(length_of_longest_substring('abcabcbb'))
print(length_of_longest_substring('bbbbb'))
print(length_of_longest_substring('pwwkew'))
print(length_of_longest_substring('pwwkeh'))
# 3
# 1
# 3
# 4