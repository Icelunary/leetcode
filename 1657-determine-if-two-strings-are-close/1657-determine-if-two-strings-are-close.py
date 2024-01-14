class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        set1 = set(word1)
        set2 = set(word2)
        cnt1 = Counter(Counter(word1).values())
        cnt2 = Counter(Counter(word2).values())
        # print(set1)
        # print(cnt1)
        # print(cnt2)
        return set1 == set2 and cnt1 == cnt2