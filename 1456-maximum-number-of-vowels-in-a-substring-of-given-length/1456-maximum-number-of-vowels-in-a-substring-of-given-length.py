class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxNums = 0
        count = 0
        for char in s[0:k]:
            if self.checkVowels(char):
                count += 1
        maxNums = count
        for index in range(k, len(s)):
            if self.checkVowels(s[index - k]):
                count -= 1
            if self.checkVowels(s[index]):
                count += 1
            if count > maxNums:
                maxNums = count
        return maxNums
            
    def checkVowels(self, char) -> bool:
        if char == "a" or char == "i" or char == "u" or char == "e" or char == "o":
            return True
        else:
            return False