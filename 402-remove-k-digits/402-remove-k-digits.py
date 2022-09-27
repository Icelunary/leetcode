class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if  k >= n:
            return "0"
        incStack = [0]
        pick = 0
        ans = ""
        for i in range(1, n):
            if pick == k:
                incStack.append(i)
                continue
            while incStack and int(num[i]) < int(num[incStack[-1]]):
                incStack.pop()
                pick += 1
                if pick == k:
                    break
            incStack.append(i)
        picked = 0
        for i in incStack:
            if picked == n - k:
                break
            if ans == "" and num[i] == "0":
                picked += 1
                continue
            else:
                ans += num[i]
                picked += 1
        return ans[:min(len(ans), n-k)] if ans != "" else "0"
        
        # TLE solution
#         n = len(num)
#         if k >= n:
#             return "0"
#         s = 0
#         ans = ""
#         # print("need pick ", n-k, "num", n)
#         for i in range(n-k):
#             left = n - k - i - 1
#             # print("left is", left, n, k, i)
#             (digit, s) = self.pickSmal(num, s, n - left)
#             s += 1
#             if digit == 0 and ans == "":
#                 continue
#             else:
#                 ans += (str(digit))
#         if ans == "":
#             return "0"
#         return ans
    
#     def pickSmal(self, num: str, s, e: int) -> (int, int):
#         mi = 10
#         idx = -1
#         for i in range(s, e):
#             digit = int(num[i])
#             if digit < mi:
#                 mi = digit
#                 idx = i
#         return mi, idx