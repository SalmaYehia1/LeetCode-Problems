# Last updated: 3/27/2026, 12:57:40 AM
1class Solution:
2    def findClosest(self, x: int, y: int, z: int) -> int:
3        a=abs(z-x)
4        b=abs(z-y)
5        if a==b:
6            return 0
7        elif a>b:
8            return 2
9        else:
10            return 1
11
12        