import re


def is_match(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    # value = re.match(p, s)
    # return False if value is None or value.group(0) != s else True

    def dfs(string, pattern, memo):
        if not pattern and string:
            return False
        if not string and pattern:
            return set(pattern[1::2]) == {"*"} and not (len(pattern) % 2)
        if (string, pattern) in memo:
            return memo[string, pattern]
        char, exp, prev = string[-1], pattern[-1], 0 if len(pattern) < 2 else pattern[-2]
        memo[string, pattern] = (
                         exp == '*' and
                         (
                             (prev in {char, '.'} and dfs(string[:-1], pattern, memo)) or
                             dfs(string, pattern[:-2], memo)
                         )
                      ) or (exp in {char, '.'} and dfs(string[:-1], pattern[:-1], memo))
        return memo[string, pattern]

    return dfs(s, p, memo={("", ""): True})


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