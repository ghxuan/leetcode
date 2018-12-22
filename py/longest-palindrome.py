def longest_palindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # # 著名的 马拉车算法
    # # t 的 长度是 len_s+len_s+3
    # # 2len_s+3 绝对是奇数
    # if s == '':
    #     return ''
    # t = f"$#{'#'.join(s)}##"
    # len_ = len(t)
    # lens = [0] * len_
    # i_center, i_right = [0] * 2
    # i_max = 1
    # for i in range(len_):
    #     # 判断 长度是否还在总长度里
    #     if len_ - 1 - i <= lens[i_max]:
    #         break
    #     # 取 lens[2*i_center-i] 与 i_right-i 的最小值
    #     lens[i] = min(lens[2 * i_center - i], i_right - i) if i < i_right else 0
    #     while t[i + lens[i] + 1] == t[i - lens[i] - 1]:
    #         lens[i] += 1
    #     # 更新 中心点
    #     if i_right < lens[i] + i:
    #         i_right = i + lens[i]
    #         i_center = i
    #     # 更新最大值 i_max 中心值
    #     if lens[i_max] < lens[i]:
    #         i_max = i
    # res = s[(i_max - lens[i_max]) // 2: (i_max + lens[i_max]) // 2]
    # return res if res else s[0]

    n = len(s)
    if n < 2 or s == s[::-1]:
        return s
    max_len = 1
    start = 0
    for i in range(1, n):
        even = s[i - max_len:i + 1]
        odd = s[i - max_len - 1:i + 1]
        if i - max_len - 1 >= 0 and odd == odd[::-1]:
            start = i - max_len - 1
            max_len += 2
            continue
        if i - max_len >= 0 and even == even[::-1]:
            start = i - max_len
            max_len += 1
    return s[start:start + max_len]


print(longest_palindrome('babad'))
print(longest_palindrome('bbl'))
print(longest_palindrome('abcdefgfedcbka'))
print(longest_palindrome('vabcdeffedcbab'))
print(longest_palindrome('abba'))
print(longest_palindrome('abcda'))
print(longest_palindrome(''))
# bab
# bb
# bcdefgfedcb
# abcdeffedcba
# abba
# a
# ''