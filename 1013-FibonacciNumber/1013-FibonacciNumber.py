# Last updated: 11/25/2025, 5:01:44 PM
class Solution(object):
    def fib(self, n):
        a,b=0,1
        for i in range(n):
            a,b=b,a+b
        return a        