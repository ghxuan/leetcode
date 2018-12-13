def longest_common_prefix(strings):
    """
    :type strings: List[str]
    :rtype: str
    """
    strings = sorted(strings)
    # print(strings)
    # python 自带的 sorted 方法
    # 是以 ASCII 排序的，
    # 那么，如果最后一个和第一个相等，
    # 则说明 所有内容相等
    start = strings[0]
    end = strings[1]
    for i, _ in enumerate(start):
        if not end.startswith(start[:i]):
            return f'"{end[:i-1]}"'
    return f'"{start}"'


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix(["dog", "dogs", "dog_pp"]))
# "fl"
# ""
# "dog"