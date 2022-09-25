class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        res = 1
        ma = 0
        cnt = 0
        pre = 0
        for num in nums:
            if num > ma:
                ma = num
                res = 1
                cnt = 1
            if num == pre and num == ma:
                cnt += 1
                res = max(res, cnt)
            if num < ma:
                cnt = 1
            
            pre = num
                
                
        return res
                