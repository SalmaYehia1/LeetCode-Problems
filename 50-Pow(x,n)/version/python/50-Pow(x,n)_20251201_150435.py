# Last updated: 12/1/2025, 3:04:35 PM
1class Solution(object):
2    def myPow(self, x, n):
3        if n==0:
4            return 1
5        if x==0:
6            return 0
7
8        if n < 0:
9            return 1 / self.myPow(x, -n)
10
11        y = self.myPow(x, n // 2)     #if odd so use //
12
13        if n%2==0:
14            return y*y
15        elif n%2==1:
16            return y*y*x
17        