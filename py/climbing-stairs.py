class Solution:
    def climbStairs(self, n: int) -> int:
        if n is 1: return 1
        elif n is 2: return 2
        a,b = 1,2
        for _ in range(n-2):
            a,b = b,a+b
        return b
