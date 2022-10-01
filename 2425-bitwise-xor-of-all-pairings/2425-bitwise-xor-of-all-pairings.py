class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        total = 0
        if n % 2:
            for i in nums2:
                total ^= i
        if m % 2:
            for i in nums1:
                total ^= i
        return total