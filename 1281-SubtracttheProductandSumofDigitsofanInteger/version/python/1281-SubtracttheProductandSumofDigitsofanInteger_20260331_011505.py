# Last updated: 3/31/2026, 1:15:05 AM
1class Solution:
2    def subtractProductAndSum(self, n: int) -> int:
3        res = [int(d) for d in str(n)]
4        s=0
5        c=1
6        for i in res:
7            s+=i
8            c*=i
9        return c-s
10        