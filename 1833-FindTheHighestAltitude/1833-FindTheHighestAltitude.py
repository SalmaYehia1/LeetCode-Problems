# Last updated: 3/8/2026, 3:16:01 PM
class Solution(object):
    def largestAltitude(self, gain):
        res=[0]
        for i in range(0,len(gain)):
            res.append(res[i]+gain[i])
    
        return max(res)
        