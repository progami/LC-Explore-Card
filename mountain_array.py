from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        
        valley = 0

        for i in range(0, len(arr)-1):
            
            if arr[i] == arr[i+1]:
                return False
 
            # check valley
            if i > 0 and i < len(arr):
                
                if (arr[i] > arr[i+1]) and (arr[i] > arr[i-1]):
                    valley += 1           
            
            # before valley - strict increase
            if valley == 0:

                if not arr[i] < arr[i+1]: 
                    return False
            
            # after valley - strict decrease
            if valley == 1:

                if not arr[i] > arr[i+1]:
                    return False
            
            # multiple valleys
            if valley > 1:
                return False
        

        if valley == 1:
            return True

print(Solution().validMountainArray([1, 2, 1]))
print()

print(Solution().validMountainArray([1, 2, 1, 2]))
print()
