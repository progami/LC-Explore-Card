class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        
        max_num = nums[0]
        max_index = 0

        for i, num in enumerate(nums):
            
            if num > max_num:
                max_num = num
                max_index = i
        
        twice_max_all = False

        for i in range(len(nums)):

            if nums[i] != max_num:
                
                temp = nums[i] * 2

                if temp > max_num:
                # a given number, is more than twice the max
                    twice_max_all = True
                
                if twice_max_all:
                    return -1
        
        # we made it here, so twice_max_all flag is still False
        return max_index


print(Solution().dominantIndex([1,2,3,4]))
print(Solution().dominantIndex([3,6,1,0]))
print(Solution().dominantIndex([0,0,0,1]))
