class Solution:
    res = []
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        print(candidates)
        self.backtrack(candidates, [], target, 0, 0)
        return self.res
        
    def backtrack(self, candidates, track, target, currentSum, index):
        if currentSum == target:
            self.res.append(track[:])
            return
        elif currentSum > target:
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i-1] == candidates[i]:
                continue
            ele =  candidates[i]
            track.append(ele)
            self.backtrack(candidates, track, target, currentSum + ele, i + 1)
            track.pop()