class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        cnt = [0 for i in range(26)]
        res = []
        p_cnt = [0 for i in range(26)]
        for i in p:
            p_cnt[ord(i) - ord("a")] += 1
        
        n = len(p)
        for i in range(0, len(p)):
            print(i)
            cnt[ord(s[i]) - ord("a")] += 1
        if cnt == p_cnt:
            res.append(0)
        for i in range(n, len(s)):
            cnt[ord(s[i]) - ord("a")] += 1
            cnt[ord(s[i-n]) - ord("a")] -= 1
            if cnt == p_cnt:
                res.append(i - n + 1)
        return res
        
            