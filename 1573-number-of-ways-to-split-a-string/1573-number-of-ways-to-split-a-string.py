class Solution:
    def numWays(self, s: str) -> int:
        num = s.count("1")
        if num % 3 != 0:
            return 0
        if num == 0:
            n = len(s)
            return ((n-1)*(n-2)//2) % (10**9+7) 
        target = num // 3
        cnt = 0
        opt1 = opt2 = 0
        for c in s:
            if c == "1":
                cnt += 1
            if cnt > target:
                if opt1 > 0 and opt2 > 0:
                    break
                cnt = 1
                opt2, opt1 = opt1, 0
            if cnt == target:
                opt1 += 1
            # print(opt1, opt2)
        # #     print(cnt)
        # print(opt1, opt2)
        return opt1 * opt2 % (10**9 + 7)