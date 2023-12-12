class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] -1) * (nums[-2]-1)
#         hi = lo = 0
#         for num in nums:
#             if num > lo:
#                 lo = num
#             if lo > hi:
#                 hi, lo = lo, hi
        
#         return (hi - 1) * (lo - 1)