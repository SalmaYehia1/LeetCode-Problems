# Last updated: 4/6/2026, 10:26:17 PM
class Solution:
    def mirrorDistance(self, n: int) -> int:
        k=int(str(n)[::-1])
        return abs(n-k)
        
