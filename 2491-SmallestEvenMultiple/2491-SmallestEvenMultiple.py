# Last updated: 4/6/2026, 10:26:41 PM
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        else:
            return n*2
        