# Last updated: 12/1/2025, 3:50:23 PM
1class Solution(object):
2    def mySqrt(self, x):
3        r = x
4        while (r * r) > x:
5            r = (r + (x // r)) // 2
6        return r
7