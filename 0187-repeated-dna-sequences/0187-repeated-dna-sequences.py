class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        record = set()
        l = 0
        r = 10
        res = set()
        while r <= len(s):
            if s[l:r] in record:
                res.add(s[l:r])
            record.add(s[l:r])
            l += 1
            r += 1
        return list(res)