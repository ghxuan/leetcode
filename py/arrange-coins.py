
def arrange_coins(n):
    """
    :type n: int
    :rtype: int
    """
    # 假如说 n 正好可以构成 k 层完整
    # (2+k-1)k/2 = n
    # k^2+k-2n=0
    # k>0 k=(-1+(1+8n)**0.5)*0.5
    # 若 最后一层不完整， 则 k 不为 整数
    # 向下取整 floor
    # 去除小数部分 int
    return int((-1+(1+8*n)**0.5)*0.5)


print(arrange_coins(5))
print(arrange_coins(8))
print(arrange_coins(1))
print(arrange_coins(3))
print(arrange_coins(6))
print(arrange_coins(10))
print(arrange_coins(15))
# 2
# 3
# 1
# 2
# 3
# 4
# 5
