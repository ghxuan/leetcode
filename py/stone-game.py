def stoneGame(piles):
    """
    :type piles: List[int]
    :rtype: bool
    """
    n = len(piles)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = piles[i]
    for left in range(n - 2, -1, -1):
        for right in range(left + 1, n):
            chose_left = piles[left] - dp[left + 1][right]
            chose_right = piles[right] - dp[left][right - 1]
            dp[left][right] = max(chose_left, chose_right)
    if dp[0][n - 1] >= 0:
        return True
    else:
        return False


print(stoneGame([5, 3, 4, 5]))
print(stoneGame([2, 2, 5, 11, 4, 1]))


# True
# True