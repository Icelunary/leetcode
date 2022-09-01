class Solution:
    def sortString(self, s: str) -> str:
        cnt = {}
        left = len(s)
        exist = [0 for i in range(26)]
        pending = []
        for i in s:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
            exist[ord(i) - ord("a")] = 1
        for i in range(26):
            if exist[i] == 1:
                pending.append(chr(i + ord("a")))
        exist = None
        
        res = ""
        index = 0
        direction = 1
        m = len(pending)
        while left:
            if cnt[pending[index]] != 0:
                res += pending[index]
                left -= 1
                cnt[pending[index]] -= 1
            if index == m - 1 and direction == 1:
                index += direction
                direction = -1
            if index == 0 and direction == -1:
                index += direction
                direction = 1
            index += direction
        return res
            
        
        
        