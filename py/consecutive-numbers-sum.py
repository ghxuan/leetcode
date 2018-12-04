from math import floor


def consecutiveNumbersSum(n):
    """
    :type n: int
    :rtype: int
    """
    # floor 向下取整
    # 假如从 1 开始，满足求和为 n ，
    # 和为：1+2+···+i = n
    # (2+i-1)i/2=n
    # i^2+i-2n=0
    # (-1+-(1-4(-2n))^0.5)*0.5
    # 那么，最大长度 i 为
    # (1+8*n)**0.5-1)*0.5
    # 当首项为 k+1 , 长度为 i 时，
    # 结果为 (k+1)+(k+2)+···+(k+i)=n
    # 那么， n-(1+2+···+i)=k*i
    # k 为整数
    # (n-(1+2+···+i))%i 一定为 0
    return len([i for i in range(1, floor(((1+8*n)**0.5-1)*0.5)+1) if not (n-(1+i)*i/2) % i])
    # 好吧， 我又想起 PEP572 了
    # return len([i for i in range(1, floor(((1+8*n)**0.5-1)*0.5)+1) if not (n:=n-i) % i])


print(consecutiveNumbersSum(5))
print(consecutiveNumbersSum(9))
print(consecutiveNumbersSum(15))
print(consecutiveNumbersSum(10 ** 9))
# 2
# 3
# 4
# 10