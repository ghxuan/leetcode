def str_str(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    return haystack.index(needle) if needle in haystack else -1


print(str_str('hello', 'll'))
print(str_str('aaaaa', 'bba'))
# 2
# -1