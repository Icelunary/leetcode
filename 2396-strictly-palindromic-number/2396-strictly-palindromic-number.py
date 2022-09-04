class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for b in range(2, n - 1):
            if not self.convertBase(n, b):
                return False
        return True
        
        # from discuss
        # just return False
    
    def convertBase(self, n, base):
        digits = []
        length  = 0
        if n == 0 :
            return 0
        while n:
            digits.append(n % base)
            n = n // base
            length += 1
        for i in range(length):
            if digits[i] != digits[length - i - 1]:
                return False
        return True    