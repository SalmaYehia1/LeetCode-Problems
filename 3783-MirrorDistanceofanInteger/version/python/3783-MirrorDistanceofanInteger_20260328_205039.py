# Last updated: 3/28/2026, 8:50:39 PM
1class Solution:
2    def mirrorDistance(self, n: int) -> int:
3        k=int(str(n)[::-1])
4        return abs(n-k)
5        
6