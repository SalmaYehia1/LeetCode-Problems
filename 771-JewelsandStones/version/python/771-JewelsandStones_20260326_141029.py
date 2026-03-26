# Last updated: 3/26/2026, 2:10:29 PM
1class Solution:
2    def numJewelsInStones(self, jewels: str, stones: str) -> int:
3        x=list(jewels)
4        y=list(stones)
5        c=0
6        res=[]
7        for i in x :
8            if i not in res:
9                c+=y.count(i)
10                res.append(i)
11        return c
12            
13
14
15
16        