class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        res = -1
        curr_len = 0
        is_alternating = False
        
        for i in range(1, len(nums)):
            if is_alternating:
                if nums[i] == nums[i-2]: # new element continues subarray
                    curr_len += 1
                else: # new element ends subarray
                    is_alternating = False
            if not is_alternating and nums[i] == nums[i-1] + 1: #start new alternating subarray
                is_alternating = True
                curr_len = 2
            res = max(res, curr_len)
        
        return res if curr_len > 0 else -1