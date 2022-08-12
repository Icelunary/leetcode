class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_level = [0] * n
        trsut_other_level = [0] * n
        for person1, person2 in trust:
            trust_level[person2 - 1] += 1
            trsut_other_level[person1 - 1] += 1
        for person in range(1, n + 1):
            if trust_level[person - 1] == n-1 and trsut_other_level[person - 1] == 0:
                return person
        return -1