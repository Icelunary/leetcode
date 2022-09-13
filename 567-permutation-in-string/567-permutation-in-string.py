class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = {}
        need = 0
        n = len(s2)
        m = len(s2)
        if n < m:
            return False
        for c in s1:
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1
            need += 1

        need_ori = need
        cnt_ori = cnt.copy()
        l = 0
        r = 0
        while r != m:
            c = s2[r]
            # if exist
            if c in cnt:
                # if still need
                if cnt[c]:
                    cnt[c] -= 1
                    need -= 1
                    if need == 0:
                        return True
                # if no need, move L
                else:
                    cnt[c] -= 1
                    need -= 1
                    while cnt[c] == -1:
                        c1 = s2[l]
                        cnt[c1] += 1
                        l += 1
                        need += 1
            else:
                need = need_ori
                cnt = cnt_ori.copy()
                l = r + 1
            r += 1
        return False