


def mySqrt(x):
    """
    :param x: int
    :return: (int, int)
    """
    if x < 0:
        return None
    if not x:
        return 0
    # 记录每轮除2的结果，并每轮的结果是以其本身除2，之后不会再计算
    sub_x = x / 2
    # 每轮的中点的取整
    sub = int(sub_x)
    # 总共运行几轮
    count = 0
    while 1:
        count += 1
        sub_left = sub ** 2
        sub_right = (sub + 1) ** 2
        if sub_left <= x < sub_right:
            return sub, count
        elif sub_right == x:
            return sub + 1, count
        else:
            temp = sub_x / 2
            if sub_x < 1:
                sub_x = 1
            elif temp > 1:
                sub_x = temp
            if sub_left > x:
                sub -= int(sub_x)
            else:
                sub += int(sub_x)


print(mySqrt(4))
print(mySqrt(10))
print(mySqrt(11))
print(mySqrt(22))
print(mySqrt(33))
print(mySqrt(44))
print(mySqrt(444))
print(mySqrt(444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444))

# (2, 1)
# (3, 2)
# (3, 2)
# (4, 3)
# (5, 5)
# (6, 3)
# (21, 10)
# (21081851067789195546659290296218123558130367595501445, 348)



def mySqrt(x):
    """
    :param x: int
    :return: (int, int)
    """
    if x < 0:
        return None
    if not x:
        return 0
    sub = x / 2
    count = 0
    while 1:
        sub_last = sub
        sub = sub/2 + x/(2*sub)
        count += 1
        if sub_last == sub:
            return int(sub), count


print(mySqrt(4))
print(mySqrt(10))
print(mySqrt(11))
print(mySqrt(22))
print(mySqrt(33))
print(mySqrt(44))
print(mySqrt(444))
print(mySqrt(444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444))


# (2, 1)
# (3, 6)
# (3, 6)
# (4, 7)
# (5, 7)
# (6, 7)
# (21, 9)
# (21081851067789195751642340792366905392191916029771776, 179)




import numpy as np


def mySqrt(x):
    """
    :param x: int
    :return: (int, int)
    """
    number = np.array([x])
    y = number.astype(np.float32)
    x2 = y * 0.5
    i = y.view(np.int32)
    i[:] = 0x5f3759df - (i >> 1)
    y = y * (1.5 - x2 * y * y)
    return y
