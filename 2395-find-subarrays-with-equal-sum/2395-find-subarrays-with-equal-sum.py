class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        record = []
        for i in range(1, len(nums)):
            record.append(nums[i-1] + nums[i])
        record.sort()
        pre = None
        for i in record:
            if i == pre:
                return True
            else:
                pre = i
        # From discuss
#         sums = set()
        
#         for i in range(len(nums)-1):
#             t = nums[i]+nums[i+1]
#             if t in sums:
#                 return True
#             else:
#                 sums.add(t)
            
#         return False