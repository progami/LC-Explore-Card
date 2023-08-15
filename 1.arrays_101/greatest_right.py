class Solution:
    
    def replaceElements(self, arr: list[int]) -> list[int]:
        
        length = len(arr)   
        temp_max = 0

        for i in range(length):
            
            if i == length - 1:
                arr[i] = -1

            for j in range(i+1, length):
                
                if arr[j] > temp_max:
                    temp_max = arr[j]

            arr[i] = temp_max

        return arr


Solution().replaceElements([17,18,5,4,6,1])
print()

Solution().replaceElements([17,18,5,4,6,1])
print()
