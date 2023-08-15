class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) < 2:
            return
        
        slow = 0
        fast = 0
        
        for fast in range(len(nums)):

            if nums[fast] != 0:
                
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp
                
                slow += 1

        print(nums)

Solution().moveZeroes([0, 1, 0, 3, 12])
