def add_digits(num):
    """
    :type num: int
    :rtype: int
    """
    # 最后结果一定是 0~9 之间循环
    # 因为 不管怎么加 0 一定不可能出现
    # 1~9
    # 取余
    # num % 9 结果只会在 0~8 之间循环
    # (num - 1) % 9 的结果
    # 也只会在 0~8 之间循环
    # 那么 (num - 1) % 9 + 1
    # num 为 0 时， 返回 0
    return (num - 1) % 9 + 1 if num else 0


print(add_digits(0))
print(add_digits(38))
print(add_digits(838))
# for i in range(10000):
#     print(i, add_digits(i))
# 0
# 2
# 1