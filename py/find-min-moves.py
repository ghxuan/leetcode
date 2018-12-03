


def findMinMoves(machines):
    """
    :type machines: List[int]
    :rtype: int
    """
    m_sum = sum(machines)
    m_len = len(machines)
    time = temp = 0
    if m_sum % m_len != 0:
        return -1
    avg = m_sum / m_len
    for m in machines:
        temp += m - avg
        print(time, temp, m - avg)
        time = max(time, abs(temp), m - avg)
    return int(time)


print(findMinMoves([1, 0, 5]))
print(findMinMoves([0, 3, 0]))
print(findMinMoves([0, 2, 0]))
print(findMinMoves([1, 7, 5, 3]))
print(findMinMoves([0, 8, 0, 0]))

# 0 -1.0 -1.0
# 1.0 -3.0 -2.0
# 3.0 0.0 3.0
# 3
# 0 -1.0 -1.0
# 1.0 1.0 2.0
# 2.0 0.0 -1.0
# 2
# -1
# 0 -3.0 -3.0
# 3.0 0.0 3.0
# 3.0 1.0 1.0
# 3.0 0.0 -1.0
# 3
# 0 -2.0 -2.0
# 2.0 4.0 6.0
# 6.0 2.0 -2.0
# 6.0 0.0 -2.0
# 6

