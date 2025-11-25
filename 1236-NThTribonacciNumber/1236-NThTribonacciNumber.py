# Last updated: 11/25/2025, 5:01:43 PM
class Solution(object):
    def tribonacci(self, n):
        a,b,c=0,1,1
        for i in range(n):
            a,b,c=b,c,a+b+c
        return a
        