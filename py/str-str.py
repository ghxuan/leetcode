def str_str(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    n = len(needle)
    for i, j in enumerate(haystack):
        if j == needle[0]:
            if haystack[i+1:i+n] == needle[1:]:
                return i
    return -1


print(str_str('hello', 'll'))
print(str_str('aaaaa', 'bba'))
# 2
# -1