def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower().strip(' ')
    if ' ' in s:
        return False
    if 'e' in s:
        strings = s.split('e')
        try:
            float(strings[0])
            int(strings[1])
        except Exception as e:
            return False
        else:
            return True
    try:
        float(s)
    except Exception as e:
        return False
    return True


print(isNumber(' -0.5 '))
print(isNumber(' 44.23 2 '))
print(isNumber('abs'))
print(isNumber(' -2.5E-10'))
print(isNumber(' -+2.5E--10'))
print(isNumber('1 a'))
# True
# False
# False
# True
# False
# False