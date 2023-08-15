class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
       
        slow = 0
        
        for fast in range(len(nums)):
            # [1, 3, 2, 4] -> fast = 2, slow = 0, [2, 3, 1, 4] -> fast = 3, slow = 1 [2, 4, 1, 3] 
            if nums[fast] % 2 == 0:
            # even
                # swap
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


        print(nums)

Solution().sortArrayByParity([3, 1, 2, 4])
