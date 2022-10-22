class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m < n:
            return ""
        cnt = Counter(t)
        # print(cnt)
        unsatisfy = sum(cnt.values())
        # print(unsatisfy)
        
        l = r = 0
        res = ""
        while r <= m:
            if unsatisfy == 0:
                c = s[l]
                if c in cnt:
                    cnt[c] += 1
                if cnt[c] > 0:
                    if r-l < len(res) or res == "":
                        res = s[l:r]
                    unsatisfy += 1
                l += 1
            else:
                if r == m:
                    break
                c = s[r]
                if c in cnt:
                    if cnt[c] > 0:
                        unsatisfy -= 1
                    cnt[c] -= 1
                r += 1
        return res


                
        
        
                
        
        
                
        
        
                
        
        
                
        
        
                
        
        
        
        
        # m = len(s)
        # n = len(t)
        # cnt = {}
        # satisfied = 0
        # for i in range(n):
        #     c = t[i]
        #     if c in cnt:
        #         cnt[c] += 1
        #     else:
        #         cnt[c] = 1
        # left, right = 0,0
        # start, end = 0,math.inf
        # while right != m:
        #     c = s[right]
        #     if c in cnt:
        #         cnt[c] -= 1
        #         if cnt[c] >= 0:
        #             satisfied += 1
        #     right += 1
        #     while satisfied == n:
        #         if s[left] in cnt:
        #             cnt[s[left]] += 1
        #             if cnt[s[left]] > 0:
        #                 satisfied -= 1
        #                 if right - left < end - start:
        #                     start, end = left, right
        #         left += 1
        # if end == math.inf:
        #     return ""
        # return s[start: end]