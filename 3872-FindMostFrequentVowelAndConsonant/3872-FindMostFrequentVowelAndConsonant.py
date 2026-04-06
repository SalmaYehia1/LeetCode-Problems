# Last updated: 4/6/2026, 10:26:09 PM
class Solution:
    def maxFreqSum(self, s: str) -> int:
        v=['a','e','u','i','o']
        c=[]
        l=[]
        list(s)
        
        for j in s:
            if j not in v :
                l.append(s.count(j))
            else:
                c.append(s.count(j))
        
        if len(c)!=0 and len(l)!=0:
            return (max(c) + max(l))
        elif len(c)==0:
            return max(l)
        else:
            return max(c)


        