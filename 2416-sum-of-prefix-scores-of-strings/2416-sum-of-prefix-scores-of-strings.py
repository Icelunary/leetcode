class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.cnt = {}
        self.dp = {}
        for word in words:
            for idx in range(len(word)):
                temp = word[:idx + 1]
                if temp in self.cnt:
                    self.cnt[temp] += 1
                else:
                    self.cnt[temp] = 1
            # print(cnt)
        res = []
        # print(cnt)
        # for word in words:
        #     total = 0
        #     for idx in range(len(word)):
        #         total += cnt[word[:idx+1]]
        #     res.append(total)
        
        for word in words:
            total = 0
            if word in self.dp:
                res.append(self.dp[word])
            else:
                res.append(self.backtrack(word))
                        
        return res
    
    def backtrack(self, word) -> int:
        if len(word) == 1:
            self.dp[word] = self.cnt[word]
            return self.dp[word]
        if word in self.dp:
            return self.dp[word]
        else:
            preSum = self.backtrack(word[:-1])
            total = preSum + self.cnt[word]
            self.dp[word] = total
            return total