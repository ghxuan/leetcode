class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(cnt, i, k, n, result, results):
            if cnt == k:
                results.append(result)
                return 
            for t in range(i, n-(k-cnt)+1, 1):
                helper(cnt+1, t + 1, k, n, result+[t+1], results)
        res = []
        helper(0, 0, k, n, [], res)
        return res
