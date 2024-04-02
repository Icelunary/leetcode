class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        record = {}
        for i in range(len(s)):
            if s[i] in record:
                if record[s[i]] != t[i]:
                    return False
            else:
                record[s[i]] = t[i]
        return True and (len(set(s)) == len(set(t)))