class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda sl: (-sl[0],-sl[1]))
        groups = []
        num = 0
        currentAtk = None
        cnt = 0
        maxDef = 0
        currentMaxDef = 0
        for atk, defense in properties:
            if atk != currentAtk:
                groups.append([])
                num += 1
                currentAtk = atk
                maxDef = max(maxDef, currentMaxDef)
            groups[-1].append([atk, defense])
            if currentMaxDef < defense: 
                currentMaxDef = defense
            if num > 0 and defense < maxDef:
                cnt += 1
        return cnt