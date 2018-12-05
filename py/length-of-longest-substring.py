def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    longest_subs = longest_sub = ''
    for i in s:
        if i in longest_sub:
            longest_sub = i
        else:
            longest_sub += i
        if len(longest_sub) >= len(longest_subs):
            longest_subs = longest_sub
    print(longest_subs)
    return len(longest_subs)


print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring('pwwkeh'))
 # abc
 # 3
 # b
 # 1
 # wke
 # 3
 # wkeh
 # 4