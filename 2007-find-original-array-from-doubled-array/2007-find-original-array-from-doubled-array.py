class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        n = len(changed)
        if n % 2 != 0 or n == 0:
            return []
        cnt = {}
        res = []
        for i in changed:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
        # print(cnt)
        # print(cnt[0])
        for idx in range(n-1, -1, -1):
            num = changed[idx]
            if num % 2 != 0 and num in cnt:
                return []
            if num % 2 == 0 and num in cnt:
                half = num // 2
                if half not in cnt:
                    return []
                else:
                    cnt[half] -= 1
                    cnt[num] -= 1
                    res.append(half)
                    if cnt[half] == 0:
                        del cnt[half]
                    # print(num)
                    # print(cnt)
                    if num != half:
                        if cnt[num] == 0:
                            del cnt[num]
        if len(cnt) == 0:
            return res
        else:
            return []