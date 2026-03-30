# Last updated: 3/31/2026, 1:00:21 AM
1class Solution:
2    def smallestEvenMultiple(self, n: int) -> int:
3        if n%2==0:
4            return n
5        else:
6            return n*2
7        