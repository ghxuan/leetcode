
def orderly_queue(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    # aaec 原本以为 aaec 之后不可能再进行变化
    # k=2  没想到
    # aaec/aeca/ecaa/eaac/aace
    return ''.join(sorted(s)) if k >= 2 else s[s.index(min(s)):]+s[:s.index(min(s))]
    # PEP572
    # return ''.join(sorted(s)) if k >= 2 else s[s.index(min(s)) as e:]+s[:e]
    # return ''.join(sorted(s)) if k >= 2 else s[e:=s.index(min(s)):]+s[:e]


print(orderly_queue('cba', 1))
print(orderly_queue('baaca', 3))
print(orderly_queue('bcddcea', 2))
# acb
# aaabc
# abccdde
