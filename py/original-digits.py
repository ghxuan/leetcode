
from functools import reduce


def originalDigits(s):
    """
    :type s: str
    :rtype: str
    """
    # zero one two three four five six seven eight nine
    #  z        w                   x          g
    #                h                   s
    #                      r    v
    #       o                                        i
    num_dict = {'z': 'zero', 'o': 'one', 'w': 'two', 'h': 'three', 'r': 'four',
                'v': 'five', 'x': 'six', 's': 'seven', 'g': 'eight', 'i': 'nine'}
    res = {}
    count = dict([(i, s.count(i)) for i in set(s)])

    def turn(unique):
        for i in unique:
            if i in count.keys():
                res[i] = count[i]
                for j in num_dict[i]:
                    count[j] -= res[i]
                    if not count[j]:
                        count.pop(j)

    # zwxg hs rv oi
    turn('zwxghsrvoi')
    if all([i == 0 for i in count.values()]):
        return '"%.0f" (%s)' % reduce(
            lambda a, b: (a[0]+b[0], a[1]+b[1]), 
            [(i, num_dict[j]) for i, j in enumerate(num_dict) 
             if j in res.keys()])
    return None


print(originalDigits('owoztneoer'))
print(originalDigits('fviefuro'))
# "3" (zeroonetwo)
# "9" (fourfive)
