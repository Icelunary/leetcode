class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        idx = 0
        if len(nums) == 1:
            return 0
        q = deque([0])
        print(q)
        startPos = 0
        count = 0
        # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0
#         i, j = 0
#         while j < len(nums):
#             jumpPos = i
#             while j <= i + nums[i]:
                
        
#         return 0
        while q:
            pos= q.pop()
            num = nums[pos]
            maxVal = 0
            newPos = -1
            if pos + num >= len(nums) - 1:
                return step + 1
            
            for i in range(startPos + 1, min(pos + num + 1, len(nums))):
                count += 1
                print("count: ", count)
                value =  i + nums[i]
                if value >= maxVal:
                    newPos = i
                    maxVal = value
            step += 1
            q.append(newPos)
            startPos = pos + num
        return step