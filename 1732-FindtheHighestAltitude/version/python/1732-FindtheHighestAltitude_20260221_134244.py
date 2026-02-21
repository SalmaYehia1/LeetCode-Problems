# Last updated: 2/21/2026, 1:42:44 PM
1class Solution(object):
2    def largestAltitude(self, gain):
3        res=[0]
4        for i in range(0,len(gain)):
5            res.append(res[i]+gain[i])
6    
7        return max(res)
8        