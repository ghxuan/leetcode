def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    # 优先匹配最后一个 key
    dict_ = {'(': ')', '[': ']', '{': '}'}
    temp = []
    for char in s:
        if char in dict_:
            temp.append(char)
        elif not temp or dict_[temp.pop()] != char:
            return False
    return not temp


print(is_valid('()'))
print(is_valid('()[]{}'))
print(is_valid(')]'))
print(is_valid('([)]'))
print(is_valid('{[]}'))
# True
# True
# False
# False
# True