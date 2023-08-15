class Solution:
    
    def sortedSquares(self, nums: list[int]) -> list[int]:

        for i in range(len(nums)):

            nums[i] *= nums[i]

        return sorted(nums)

Solution().sortedSquares([-4, -1, 0, 3, 10])
