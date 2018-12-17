def letter_combinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    digits_dict = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz',
    }
    res = list(digits_dict[digits[0]])
    for i in digits[1:]:
        temp1 = len(digits_dict[i]) * res
        temp2 = list(digits_dict[i]) * len(res)
        # res = [n+temp2[m] for m, n in enumerate(temp1)]
        # map 是个好东西， 比 for 循环快
        res = list(map(lambda x, y: x + y, temp1, temp2))
    return res


print(letter_combinations('23'))
print(letter_combinations('234'))
print(letter_combinations('23443564654654'))
# ['ad', 'be', 'cf', 'ad', 'be', 'cf', 'ad', 'be', 'cf']
# ['adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi']