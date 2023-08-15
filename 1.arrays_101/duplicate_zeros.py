class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                arr.insert(i, 0)  # insert zero
                arr.pop()  # maintain length of list
                i += 1  # skip next zero
            i += 1

# create an instance of the Solution class
solution = Solution()

# call duplicateZeros on that instance
solution.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
solution.duplicateZeros([0, 0, 1, 0])

