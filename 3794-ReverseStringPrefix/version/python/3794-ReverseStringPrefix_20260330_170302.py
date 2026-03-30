# Last updated: 3/30/2026, 5:03:02 PM
1class Solution:
2    def reversePrefix(self, s: str, k: int) -> str:
3        res=""
4        res+=s[k-1::-1]
5        res+=s[k:]
6        return res
7        
8        