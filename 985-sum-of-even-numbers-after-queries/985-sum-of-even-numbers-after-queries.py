class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = 0
        n = len(nums)
        for num in nums:
            if num % 2 == 0:
                total += num
        
        res = []
        for num, idx in queries:
            if nums[idx] % 2:
                nums[idx] += num
            else:
                total -= nums[idx]
                nums[idx] += num
            
            if not nums[idx] % 2:
                total += nums[idx]
            
            res.append(total)
        
        return res