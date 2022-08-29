class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

    
        nums.sort()
        temp = queries[:]
        temp.sort()
        n = len(nums)
        total = 0
        index = 0
        cnt = 0
        res = []
        temp_res = {}
        for q in temp:
            for inx in range(index, n):
                if total + nums[inx] <= q:
                    cnt += 1
                    total += nums[inx]
                else:
                    break
                index += 1
            temp_res[q] = cnt
        for i in queries:
            res.append(temp_res[i])
        return res