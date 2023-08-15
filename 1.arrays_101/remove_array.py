from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
        # start iterating from 2nd element
        i = 1
        
        length = len(nums)
        k = 0
        
        # first element is always unique
        d_count = 0
        
        if length == 1:
            k += 1
            return k

        # iterate array from start to finish
        while i < length:
   
            print(k, nums)
            
            if nums[i-1] == -999:
                break

            # last element
            if i + 1 > length - 1:
                # if last element                
                print('True')
                # and running duplicates , 3, 3, 3], shift-left, up unique counter and break
                if nums[i-1] == nums[i]:
                    d_count += 1
                    self.left_shift(nums, i + 1 - d_count, d_count)
                    # if last two elements are same, then unique counter +=1
                    k += 1
                else:
                # if not running duplicates then, ,3, 3, 4] - last element is unique, up unique counter and break
                    # since last two elements are different - then unique counter += 2
                    if nums[i] == -999:
                        k+=1
                    else:
                        k += 2
                    self.left_shift(nums, i - d_count, d_count) 
                
                break

            if (nums[i-1] == nums[i]):
                # duplicate number
                d_count += 1
            else:
                # new number
                # left shift by d_count before we start tracking new number 
                self.left_shift(nums, i - d_count, d_count)
                
                i -= d_count
                # set d_count to zero to start tracking new unique number
                d_count = 0
                k += 1 

            i += 1
        
        print('final: ', k, nums)
        return k

    def left_shift(self, nums: List[int], index: int, d_count: int) -> int:
        # left shift by d_count places
        
        length = len(nums)
        
        while d_count > 0:
            
            for i in range(index, length):
                if i+1 < length:
                    nums[i] = nums[i+1]
                else:
                    nums[i] = -999
            
            d_count -= 1

Solution().removeDuplicates([1, 1])
print()
Solution().removeDuplicates([1, 2])
print()
Solution().removeDuplicates([1, 1, 2])
print()
Solution().removeDuplicates([1, 1, 2, 2])
print()
