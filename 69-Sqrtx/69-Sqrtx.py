# Last updated: 12/2/2025, 2:12:00 AM
class Solution(object):
    def mySqrt(self, x):
        r = x
        while (r * r) > x:
            r = (r + (x // r)) // 2
        return r
