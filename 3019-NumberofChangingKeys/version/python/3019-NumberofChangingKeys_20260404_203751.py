# Last updated: 4/4/2026, 8:37:51 PM
1class Solution:
2    def countKeyChanges(self, s: str) -> int:
3        s=s.lower()
4        
5        c=0
6        for i in range(len(s)-1):
7            if s[i]!=s[i+1]:
8                c+=1
9
10        return c