class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        idx = 0
        match = {}
        record = set()
        if len(pattern) != len(words):
            return False
        while idx < len(pattern):
            word = words[idx]
            if pattern[idx] in match:
                toMatch = match[pattern[idx]]
                if word != toMatch:
                    return False
            else:
                if word in record:
                    return False
                match[pattern[idx]] = word
            record.add(word)
            
            idx += 1
                
        return True