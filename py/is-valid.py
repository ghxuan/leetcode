def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    # 优先匹配最后一个 key
    dic = {'(': ')', '[': ']', '{': '}'}
    key = list(dic.keys())
    temp = []
    for i in s:
        if i in key:
            temp.append(i)
        elif dic[temp[-1]] != i:
            return False
        else:
            temp.pop()
    return True


print(is_valid('()'))
print(is_valid('()[]{}'))
print(is_valid('(]'))
print(is_valid('([)]'))
print(is_valid('{[]}'))
# True
# True
# False
# False
# True