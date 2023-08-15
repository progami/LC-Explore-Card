from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
       
        length = len(arr)

        for i in range(length):
            for j in range(length):
                
                if not i is j:
                    
                    if arr[i] == 2 * arr[j]:
                        return True


        return False



print(Solution().checkIfExist([1, 2, 3, 4]))
print(Solution().checkIfExist([1, 2, 3, 4]))

