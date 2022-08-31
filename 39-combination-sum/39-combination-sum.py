class Solution:
    res = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.backtrack(candidates, [], target, 0, 0)
        return self.res
        
    def backtrack(self, candidates, track, target, currentSum, index):
        if currentSum == target:
            # print("ok", track, index)
            self.res.append(track[:])
            # print(self.res)
            return
        elif currentSum > target:
            # print("out", track, currentSum, index)
            return
        
        for i in range(index, len(candidates)):
            ele =  candidates[i]
            track.append(ele)
            currentSum += ele
            self.backtrack(candidates, track, target, currentSum, i)
            track.pop()
            currentSum -= ele
