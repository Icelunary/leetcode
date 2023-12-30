class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cMap = defaultdict(int)
        num = len(words)
        for word in words:
            for c in word:
                cMap[c] += 1
        for c in cMap:
            if cMap[c] % num != 0:
                return False
        return True