class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # solution from discuss, O(n), greedy
        maxAttack = max(a for a, _ in properties)
        maxDefense = [0] * (maxAttack+2)
        print(maxDefense)
        for a, b in properties:
            maxDefense[a] = max(maxDefense[a], b)
        
        for i in reversed(range(len(maxDefense)-1)):
            print(i)
            maxDefense[i] = max(maxDefense[i], maxDefense[i+1])
        
        ans = 0
        for a, b in properties:
            if b < maxDefense[a+1]:
                ans += 1
        return ans
        
        # my solution, nlogn
        # properties.sort(key=lambda sl: (-sl[0],-sl[1]))
        # groups = []
        # num = 0
        # currentAtk = None
        # cnt = 0
        # maxDef = 0
        # currentMaxDef = 0
        # for atk, defense in properties:
        #     if atk != currentAtk:
        #         groups.append([])
        #         num += 1
        #         currentAtk = atk
        #         maxDef = max(maxDef, currentMaxDef)
        #     groups[-1].append([atk, defense])
        #     if currentMaxDef < defense: 
        #         currentMaxDef = defense
        #     if num > 0 and defense < maxDef:
        #         cnt += 1
        # return cnt