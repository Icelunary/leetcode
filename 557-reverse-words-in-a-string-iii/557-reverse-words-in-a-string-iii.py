class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        temp = ""
        for c in s:
            if c != " ":
                temp += c
            else:
                res += temp[::-1]
                res += " "
                temp = ""
        res += temp[::-1]
        return res
    
        