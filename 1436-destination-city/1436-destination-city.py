class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        notEnd = set()
        for s, _ in paths:
            notEnd.add(s)
        
        for _, e in paths:
            if e not in notEnd:
                return e
            
        return "test"
        