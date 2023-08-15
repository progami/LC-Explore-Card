class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        
        total = 0
        left = 0
        current = 0
        right = 0
        none_flag = True
        
        if len(nums) == 1:
            return 0
        
        for num in nums:

            total += num
        
        running_total = 0
        
        for i in range(len(nums)):
            
            if i:
                left += nums[i-1]
                current = nums[i]
                right = total - left - current
                
                print ('index: {}, left: {}, current: {}, right: {}'\
                       .format(i, left, current, right))

                if left == right:
                    none_flag = False
                    return i
            else:
                left = 0
                current = nums[0]
                right = total - current

                if left == right:
                    none_flag = False
                    return 0
        
        if none_flag:
            return -1



# Solution().pivotIndex([1,7,3,6,5,6])
# Solution().pivotIndex([1,7,3,6,5,6])
print(Solution().pivotIndex([2, 1, -1]))
