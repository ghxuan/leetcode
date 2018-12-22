import re


def is_match(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    value = re.match(p, s)
    return False if value is None or value.group(0) != s else True


print(is_match('aa', 'a'))
print(is_match('aa', 'a*'))
print(is_match('ab', '.*'))
print(is_match('aab', 'c*a*b'))
print(is_match('mississippi', 'miss*is*p*.'))
print(is_match('', ''))
print(is_match("abcd", "d*"))
# False
# True
# True
# True
# False
# True
# False