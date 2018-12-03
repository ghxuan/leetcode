


def validSquare(p1, p2, p3, p4):
    """
    :type p1: List[int]
    :type p2: List[int]
    :type p3: List[int]
    :type p4: List[int]
    :rtype: bool
    """
    p1, p2, p3, p4 = Vector(p1), Vector(p2), Vector(p3), Vector(p4)
    p12 = p2 - p1
    p13 = p3 - p1
    p14 = p4 - p1
    p24 = p4 - p2
    p34 = p4 - p3
    p23 = p3 - p2
    p = [p12, p13, p14, p24, p34, p23]
    # set的结果是一组无序排列的可哈希的值。
    # 这个类必须要可哈希，所以必须要有__hash__这个魔术方法。
    # set通过__eq__这个魔术方法判断是否相等，是否可以被添加。
    list_p = list(Set(p))
    if len(list_p) == 2:
        if p.count(list_p[0]) == 2 or p.count(list_p[0]) == 4:
            return True
    return False


class Vector(object):
    def __init__(self, a, b=0):
        self.a = a
        self.b = b
        if hasattr(a, '__iter__'):
            self.a = a[0]
            self.b = a[1]
        # 向量模的平方
        self.len = self.a * self.a + self.b * self.b

    # 返回一个可以用来表示对象的可打印字符串, 用于显示给用户。在print下显示
    def __str__(self):
        return f'({self.a}, {self.b})'

    # 返回一个可以用来表示对象的可打印字符串, 用于显示给开发人员。在[],{}和其他情况下显示。
    def __repr__(self):
        return f'({self.a}, {self.b})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return hash(id(self.len)) == hash(id(other.len))
        return False

    def __hash__(self):
        return hash(id(self.len))

    # 实现向量的减法
    def __sub__(self, other):
        a = self.a - other.a
        b = self.b - other.b
        return Vector(a, b)


class Set(set):
    def __repr__(self, *args, **kwargs):
        string = ', '.join([str(i.len) for i in self])
        return f'{{{string}}}'


print(validSquare([0, 0], [0, 1], [1, 0], [1, 1]))
print(validSquare([0, -1], [0, 1], [1, 0], [-1, 0]))
print(validSquare([900, -1], [900, 1], [901, 0], [899, 0]))

# True
# True
# True

