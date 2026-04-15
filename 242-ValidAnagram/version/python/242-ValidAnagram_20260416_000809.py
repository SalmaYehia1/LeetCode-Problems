# Last updated: 4/16/2026, 12:08:09 AM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s)!=len(t):
4            return False
5        else:
6            
7            if sorted(s)==sorted(t):
8                return True
9            else:
10                return False
11        