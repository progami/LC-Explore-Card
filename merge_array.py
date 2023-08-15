class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_pop = len(nums1) - m
        n_pop = len(nums2) - n
        
        for _ in range(m_pop):
            nums1.pop()

        for _ in range(n_pop):
            nums2.pop()
        
        nums1.extend(nums2)
        
        nums1.sort()

        print(nums1)


sol = Solution()
sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
