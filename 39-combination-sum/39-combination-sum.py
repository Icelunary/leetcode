class Solution:
    res = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.backtrack(candidates, [], target, 0, 0)
        return self.res
        
    def backtrack(self, candidates, track, target, currentSum, index):
        if currentSum == target:
            self.res.append(track[:])
            return
        elif currentSum > target:
            return
        
        for i in range(index, len(candidates)):
            ele =  candidates[i]
            track.append(ele)
            self.backtrack(candidates, track, target, currentSum + ele, i)
            track.pop()
