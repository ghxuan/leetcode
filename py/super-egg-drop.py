def superEggDrop(K, N):
    """
    :type K: int
    :type N: int
    :rtype: int
    """
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    for i in range(N+1):
        dp[1][i] = i
    for i in range(2, K+1):
        for j in range(1, N+1):
            minimum = float('inf')
            for x in range(1, j+1):
                minimum = min(minimum, (1 + max(dp[i][j - x], dp[i - 1][x - 1])))
            dp[i][j] = minimum
    return dp[K][N]


print(superEggDrop(4, 10))
print(superEggDrop(1, 2))
print(superEggDrop(2, 6))
print(superEggDrop(3, 14))
print(superEggDrop(2, 50))

# 4
# 2
# 3
# 4
# 10