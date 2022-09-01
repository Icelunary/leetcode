class Solution:
    def sortString(self, s: str) -> str:
        incre = True
        output = ''
        while(s):
            temp_s = set(s)
            if incre:
                output += "".join(sorted(temp_s))
                incre = False
            else:
                output += "".join(sorted(temp_s, reverse=True))
                incre = True
            for i in set(s):
                s = s.replace(i,"",1) 
        return output
            
        
        
        