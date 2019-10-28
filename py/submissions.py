class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        if not len(nums): return [[]]
        res = []
        for sub in self.subsets(nums[1:]):
            res.append(sub)
            res.append([nums[0]]+ sub)
        return res

class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        res = []
        for i in range(2 ** len(nums)):
            res.append([nums[x] for x, y in enumerate(bin(i)[:1:-1]) if y == '1'])
        return res
