# Last updated: 4/6/2026, 10:26:27 PM
class Solution:
    def convertDateToBinary(self, m: str) -> str:
        
        n=m.split("-")
        s=""
        for i in n:
            s+=(bin(int(i))[2:])
            s+="-"
        return s[:-1]
        
        
        
        