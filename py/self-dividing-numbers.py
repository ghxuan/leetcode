

def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    return [num for num in range(left, right+1) 
            if all([int(i) and num % int(i) == 0 for i in str(num)])]


print(selfDividingNumbers(1, 10000))
print(selfDividingNumbers(1, 22))

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
