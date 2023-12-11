class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = set()
        res = 0
        for num in nums:
            record.add(num)
        
        for num in nums:
            if num in record:
                record.remove(num)
                length = 1
                left = right = num
                while left - 1 in record:
                    left -= 1
                    record.remove(left)
                    length += 1
                while right + 1 in record:
                    right += 1
                    record.remove(right)
                    length += 1
                res = max(res, length)
                
        return res
        