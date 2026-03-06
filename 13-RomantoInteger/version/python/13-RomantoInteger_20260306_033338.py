# Last updated: 3/6/2026, 3:33:38 AM
1class Solution(object):
2    def romanToInt(self, s):
3        res=0
4        n=len(s)
5        s+="a"
6
7        for i in range(n):
8            if self.map_roman(s[i])>=self.map_roman(s[i+1]):
9                res+=self.map_roman(s[i])
10            else:
11                res-=self.map_roman(s[i])
12
13
14        return res 
15
16    def map_roman(self, c):
17        match c.upper():
18            case "I":
19                return 1
20            case "V":
21                return 5
22            case "X":
23                return 10
24            case "L":
25                return 50
26            case "C":
27                return 100
28            case "D":
29                return 500
30            case "M":
31                return 1000
32            case _:
33                return 0
34        
35       
36
37
38
39      
40        