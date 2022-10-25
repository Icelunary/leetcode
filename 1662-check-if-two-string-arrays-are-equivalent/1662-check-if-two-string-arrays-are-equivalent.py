class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string = ""
        for word in word1:
            for c in word:
                string += c
        idx = 0
        for word in word2:
            for c in word:
                if idx >= len(string) or string[idx] != c:
                    return False
                idx += 1
        if idx != len(string):
            return False
        return True