from typing import List, Set
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not len(nums): return [[]]
        res = []
        for sub in self.subsets(nums[1:]):
            res.append(sub)
            res.append([nums[0]]+ sub)
        return res
