# Last updated: 11/25/2025, 5:01:56 PM
class Solution(object):
    def fib(self,m):
        a,b=0,1
        for i in range(m):
            a,b=b,a+b
        return a
    def climbStairs(self, n):
        return self.fib(n+1) 
        