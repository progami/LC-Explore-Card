class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        max_sorted = sorted(nums)
        
        slow = 1

        # remove duplicates
        for fast in range(1, len(max_sorted)):
            
            if max_sorted[fast] != max_sorted[fast-1]:
                max_sorted[slow] = max_sorted[fast]
                slow += 1

        max_sorted = max_sorted[:slow]
        print(max_sorted)

        if len(max_sorted) >= 3:
            return max_sorted[-3]
        else:
            return max_sorted[-1]





print(Solution().thirdMax([1, 1, 1]))
