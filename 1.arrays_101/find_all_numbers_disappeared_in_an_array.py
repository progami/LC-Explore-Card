class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        
        for i in range(n):
            
            num = abs(nums[i]) - 1
            
            if nums[num] > 0:
                nums[num] *= -1


        missing_numbers = [i + 1 for i, num in enumerate(nums) if num > 0]
        
        return missing_numbers

Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
