# Last updated: 3/27/2026, 12:52:55 AM
1class Solution:
2    def maxFreqSum(self, s: str) -> int:
3        v=['a','e','u','i','o']
4        c=[]
5        l=[]
6        list(s)
7        
8        for j in s:
9            if j not in v :
10                l.append(s.count(j))
11            else:
12                c.append(s.count(j))
13        
14        if len(c)!=0 and len(l)!=0:
15            return (max(c) + max(l))
16        elif len(c)==0:
17            return max(l)
18        else:
19            return max(c)
20
21
22        