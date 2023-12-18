class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        lo1 = lo2 = hi1 = hi2 = -1
        for num in nums:
            if num > hi1:
                hi2 = hi1
                hi1 = num
            elif num > hi2:
                hi2 = num
            if num < lo1 or lo1 == -1:
                lo2 = lo1
                lo1 = num
            elif num < lo2 or lo2 == -1:
                lo2 = num
            # print(lo1, lo2, hi2, hi1)
        # print(lo1, lo2, hi2, hi1)
        return (hi1 * hi2) - (lo1 * lo2)