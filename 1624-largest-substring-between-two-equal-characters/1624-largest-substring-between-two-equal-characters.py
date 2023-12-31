class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mySet = defaultdict(int)
        ans = -1
        for i in range(len(s)):
            c = s[i]
            if c in mySet:
                ans = max(ans, i - 1 - mySet[c])
            else:
                mySet[c] = i
        return ans