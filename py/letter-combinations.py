def letter_combinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []
    digits_dict = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz',
    }
    res = digits_dict[digits[0]]
    for digit in digits[1:]:
        # temp1 = len(digits_dict[digit]) * res
        # temp2 = sorted(digits_dict[digit] * len(res))
        # res = list(map(lambda x, y: x + y, temp1, temp2))
        res = [one + two for one in res for two in digits_dict[digit]]
    return res


print(letter_combinations('23'))
print(letter_combinations('234'))
print(letter_combinations('23443564654654'))
# ['ad', 'be', 'cf', 'ad', 'be', 'cf', 'ad', 'be', 'cf']
# ['adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi', 'adg', 'beh', 'cfi']