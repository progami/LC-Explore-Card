class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        slow = 0
        
        for fast in range(len(nums)):

            if nums[fast] != val:
                
                nums[slow] = nums[fast]
                slow += 1
        
        print(nums)
        return slow



print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
