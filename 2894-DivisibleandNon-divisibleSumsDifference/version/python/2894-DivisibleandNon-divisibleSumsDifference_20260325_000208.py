# Last updated: 3/25/2026, 12:02:08 AM
1class Solution:
2    def differenceOfSums(self, n: int, m: int) -> int:
3        k=0
4        c=0
5        for i in range(n+1):
6            if i%m==0:
7                c+=i
8            else:
9                k+=i
10        return k-c
11
12        