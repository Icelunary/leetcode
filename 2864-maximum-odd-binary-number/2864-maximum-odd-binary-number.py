class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        num = s.count("1")
        if num == 0:
            return s
        ans = ""
        ans = "1" * (num - 1) + "0" * (n - num) + "1"
        
                
        
        return ans