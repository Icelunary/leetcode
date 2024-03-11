class Solution:
    def customSortString(self, order: str, s: str) -> str:
        record = Counter(s)
        ans = ""
        for c in order:
            while record[c]:
                ans += c
                record[c] -= 1
            del record[c]
        for c in record:
            while record[c]:
                ans += c
                record[c] -= 1
                
        return ans