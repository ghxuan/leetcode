def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    return int(''.join([str(i) for i in digits])) + 1


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
# 124
# 4322