# Last updated: 12/2/2025, 2:11:59 AM
class Solution(object):
    def myPow(self, x, n):
        if n==0:
            return 1
        if x==0:
            return 0

        if n < 0:
            return 1 / self.myPow(x, -n)

        y = self.myPow(x, n // 2)     #if odd so use //

        if n%2==0:
            return y*y
        elif n%2==1:
            return y*y*x
        