
def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    is_primes = [True]*(n+1)
    # 将 0 和 1 都去掉
    is_primes[0] = is_primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_primes[i]:
            # 当前面的数据都已经处理过后，最开始的一定是 i 的 i 倍
            for j in range(i**2, n+1, i):
                is_primes[j] = False
    # print([j for j, i in enumerate(is_primes) if i])
    return len([i for i in is_primes if i])


print(countPrimes(10))
# 4
