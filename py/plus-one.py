def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    # return [int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]
    for i in range(1, len(digits) + 1):
        if digits[-i] < 9:
            digits[-i] += 1
            return digits
        digits[-i] = 0
    return [1] + digits


print(plusOne([1, 2, 9]))
print(plusOne([9, 9, 9]))
print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
# [1, 3, 0]
# [1, 0, 0, 0]
# [1, 2, 4]
# [4, 3, 2, 2]
