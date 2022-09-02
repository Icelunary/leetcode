class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loseNum = {}
        
        for match in matches:
            winner = match[0]
            loser = match[1]
            if winner not in loseNum:
                loseNum[winner] = 0
            if loser in loseNum:
                loseNum[loser] += 1
            else:
                loseNum[loser] = 1
        res = [[], []]
        for player in loseNum:
            if loseNum[player] == 0:
                res[0].append(player)
            elif loseNum[player] == 1:
                res[1].append(player)
        res[0].sort()
        res[1].sort()
        return res