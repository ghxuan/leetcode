def longest_common_prefix(strings):
    """
    :type strings: List[str]
    :rtype: str
    """
    # if len(strings) == 0:
    #     return ""
    # res = strings[0]
    # for string in strings[1:]:
    #     while not string.startswith(res):
    #         res = res[:-1]
    #         if res == "":
    #             return res
    # return res

    strings = list(zip(*strings))
    res = ''
    for string in strings:
        if len(set(string)) == 1:
            res += string[0]
        else:
            break
    return res


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix(["dog", "dogs", "dog_pp"]))
# fl
#
# dog