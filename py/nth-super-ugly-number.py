def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    all_num = [1 for _ in range(n)]
    len_p = len(primes)
    range_p = range(len_p)
    x = [0 for _ in range_p]
    for i in range(1, n):
        min_list = [primes[j] * all_num[x[j]] for j in range_p]
        all_num[i] = min(min_list)
        x[min_list.index(all_num[i])] += 1
        while len(set(min_list)) < len_p:
            min_list = [primes[j] * all_num[x[j]] for j in range_p]
            if all_num[i] == min(min_list):
                x[min_list.index(min(min_list))] += 1
            else:
                break
        print('all', all_num)
    return all_num[-1]


print(nthSuperUglyNumber(12, [2, 3, 17]))
print(nthSuperUglyNumber(12, [2, 7, 13, 19]))

# all [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# all [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# all [1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1]
# all [1, 2, 3, 4, 6, 1, 1, 1, 1, 1, 1, 1]
# all [1, 2, 3, 4, 6, 8, 1, 1, 1, 1, 1, 1]
# all [1, 2, 3, 4, 6, 8, 9, 1, 1, 1, 1, 1]
# all [1, 2, 3, 4, 6, 8, 9, 12, 1, 1, 1, 1]
# all [1, 2, 3, 4, 6, 8, 9, 12, 16, 1, 1, 1]
# all [1, 2, 3, 4, 6, 8, 9, 12, 16, 17, 1, 1]
# all [1, 2, 3, 4, 6, 8, 9, 12, 16, 17, 18, 1]
# all [1, 2, 3, 4, 6, 8, 9, 12, 16, 17, 18, 24]
# 24
# all [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# all [1, 2, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# all [1, 2, 4, 7, 1, 1, 1, 1, 1, 1, 1, 1]
# all [1, 2, 4, 7, 8, 1, 1, 1, 1, 1, 1, 1]
# all [1, 2, 4, 7, 8, 13, 1, 1, 1, 1, 1, 1]
# all [1, 2, 4, 7, 8, 13, 14, 1, 1, 1, 1, 1]
# all [1, 2, 4, 7, 8, 13, 14, 16, 1, 1, 1, 1]
# all [1, 2, 4, 7, 8, 13, 14, 16, 19, 1, 1, 1]
# all [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 1, 1]
# all [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 1]
# all [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
# 32