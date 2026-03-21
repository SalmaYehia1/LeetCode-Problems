# Last updated: 3/21/2026, 1:23:09 PM
1class Solution:
2    def scoreOfString(self, s: str) -> int:
3        k=0
4        for i in range(len(s)-1):
5            k+=abs(ord(s[i])-ord(s[i+1]))
6        return k
7
8        