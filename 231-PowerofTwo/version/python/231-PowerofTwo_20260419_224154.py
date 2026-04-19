# Last updated: 4/19/2026, 10:41:54 PM
1class Solution:
2    def isPowerOfTwo(self, n: int) -> bool:
3        
4        return n > 0 and (n & (n - 1)) == 0