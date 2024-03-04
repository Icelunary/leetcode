class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        if not n:
            return n
        l = 0
        r = n - 1
        score = 0
        res = 0
        flip = 0
        
        while l <= r:
            if tokens[l] <= power:
                score += 1
                power -= tokens[l]
                # print("up ", tokens[l])
                l += 1
            elif score == 0:
                break
            else:
                score -= 1
                power += tokens[r]
                # print("down ", tokens[r])
                r -= 1
            res = max(res, score)
            
        return res