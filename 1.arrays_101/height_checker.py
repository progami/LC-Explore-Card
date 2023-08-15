class Solution:
    def heightChecker(self, heights: list[int]) -> int:

        expected = sorted(heights)
        slow = 0

        for fast in range(len(heights)):

            if expected[fast] != heights[fast]:
                slow += 1
        
        print(slow)
        return slow





Solution().heightChecker([1, 1, 4, 2, 1, 3])
