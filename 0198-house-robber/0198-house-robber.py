class Solution:
    def rob(self, nums: List[int]) -> int:
        skip = 0
        select = 0
        for num in nums:
            skip, select = max(select, skip), skip + num
        return max(select, skip)