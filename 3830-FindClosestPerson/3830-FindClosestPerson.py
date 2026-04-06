# Last updated: 4/6/2026, 10:26:22 PM
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a=abs(z-x)
        b=abs(z-y)
        if a==b:
            return 0
        elif a>b:
            return 2
        else:
            return 1

        