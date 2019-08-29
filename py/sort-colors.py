class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, cur, blue = 0, 0, len(nums) - 1
        while cur <= blue:
            if nums[cur] == 0:
                nums[cur], nums[red] = nums[red], nums[cur]
                cur, red = cur + 1, red + 1
            elif nums[cur] == 2:
                nums[cur], nums[blue] = nums[blue], nums[cur]
                blue -= 1
            else:
                cur += 1
        print(nums)


s = Solution()
s.sortColors([2, 0, 2, 1, 1, 0])
s.sortColors([0, 1, 2, 1, 1, 0])
s.sortColors([2, 0, 0, 1, 1, 0])
s.sortColors([])
