class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        l, r = 0, n - 1
        score = 0
        ans = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
            elif score == 0:
                break
            else:
                power += tokens[r]
                score -= 1
                r -= 1
            ans = max(ans, score)
        
        return ans