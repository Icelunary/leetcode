class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        # from discuss
        left = 0
        last_min_k_index = -1
        last_max_k_index = -1
        fixed_bounds_subarrays = 0

        for right, v in enumerate(nums):
            if v < minK or v > maxK:
                left = right + 1
            else:
                if v == minK:
                    last_min_k_index = right
                if v == maxK:
                    last_max_k_index = right
                if last_min_k_index >= left and last_max_k_index >= left:
                    fixed_bounds_subarrays += min(last_min_k_index, last_max_k_index) - left + 1

        return fixed_bounds_subarrays
    
    
        for i in range(len(nums)):
            num = nums[i]
            if num < minK or num > maxK:
                nums[i] = 0
        # print(nums)
        # print()
        # record = set()
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))] # [satisfy, #minK, #maxK]
        for r in range(len(nums)):
            con1 = con2 = 0
            for c in range(r, len(nums)):
                if nums[c] == 0:
                    con1 = con2 = 0
                    break
                if nums[c] == minK:
                    con1 = 1
                if nums[c] == maxK:
                    con2 = 1
                if con1 and con2:
                    dp[r][c] = 1
        # print(len(record))
        # for i in dp:
        #     print(i)
        tot = 0
        for row in dp:
            tot += sum(row)
        return tot
