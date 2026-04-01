# Last updated: 4/1/2026, 6:29:49 PM
1class Solution:
2    def convertDateToBinary(self, m: str) -> str:
3        
4        n=m.split("-")
5        s=""
6        for i in n:
7            s+=(bin(int(i))[2:])
8            s+="-"
9        return s[:-1]
10        
11        
12        
13        