class Solution:
    def makeGood(self, s: str) -> str:
        res = ""
        for c in s:
            if not res:
                res += c
            else:
                if res[-1].lower() == c.lower() and res[-1] != c:
                    res = res[:-1]
                else:
                    res += c
            # print(res)
        return res