# Last updated: 3/18/2026, 4:10:54 AM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        b = bin(n)[2:]
4        c=0
5        for i in range(len(b)):
6            if b[i]=='1':
7                c+=1
8        return c
9
10        