class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        hi = lo = 0
        for num in nums:
            if num > lo:
                lo = num
            if lo > hi:
                hi, lo = lo, hi
        
        return (hi - 1) * (lo - 1)