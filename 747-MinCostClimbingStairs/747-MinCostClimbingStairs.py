# Last updated: 12/3/2025, 9:03:14 AM
class Solution(object):
    def minCostClimbingStairs(self,c):
        n=len(c)
        c.append(0)
        for i in range(n-2,-1,-1):
            
            c[i]=min(c[i]+c[i+1],c[i]+c[i+2])
        return min(c[0],c[1])
        