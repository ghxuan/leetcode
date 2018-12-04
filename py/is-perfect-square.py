def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    # 完全平方数的末位数只能是0,1,4,5,6,9。
    last_num = '014569'
    string = str(num)
    if string[-1] in last_num:
        # n*n = (2*n-1)+(2*n-3)+(2*n-7)+...+5+3+1
        # 总共加n次
        for i in range(1, num, 2):
            num -= i
            if num == 0:
                print(f'{string}是完全平方数，是{int((i+1)/2)}的平方。')
                return True
            elif num < 0:
                print(f'{string}不是完全平方数，共计算{int((i+1)/2)}次。')
                return False
    print(f'{string}不是完全平方数，共计算0次。')
    return False


print(isPerfectSquare(25))
print(isPerfectSquare(81))
print(isPerfectSquare(99980001))
print(isPerfectSquare(99980000))
print(isPerfectSquare(99980004))
print(isPerfectSquare(3))

# 25是完全平方数，是5的平方。
# True
# 81是完全平方数，是9的平方。
# True
# 99980001是完全平方数，是9999的平方。
# True
# 99980000不是完全平方数，共计算9999次。
# False
# 99980004不是完全平方数，共计算10000次。
# False
# 3不是完全平方数，共计算0次。
# False