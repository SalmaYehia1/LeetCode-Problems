# Last updated: 4/6/2026, 10:27:45 PM
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = [int(d) for d in str(n)]
        s=0
        c=1
        for i in res:
            s+=i
            c*=i
        return c-s
        