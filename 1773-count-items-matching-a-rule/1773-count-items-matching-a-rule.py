class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        for item in items:
            value = None
            if ruleKey == "type":
                value = item[0]
            elif ruleKey == "color":
                value = item[1]
            elif ruleKey == "name":
                value = item[2]
            if value == ruleValue:
                cnt += 1
        return cnt