# Last updated: 3/8/2026, 3:16:36 PM
class Solution(object):
    def romanToInt(self, s):
        res=0
        n=len(s)
        s+="a"

        for i in range(n):
            val=self.map_roman(s[i])
            if val>=self.map_roman(s[i+1]):
                res+=val
            else:
                res-=val


        return res 

    def map_roman(self, c):
        match c.upper():
            case "I":
                return 1
            case "V":
                return 5
            case "X":
                return 10
            case "L":
                return 50
            case "C":
                return 100
            case "D":
                return 500
            case "M":
                return 1000
            case _:
                return 0
        
       



      
        