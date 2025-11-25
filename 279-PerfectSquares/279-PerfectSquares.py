# Last updated: 11/25/2025, 5:01:49 PM
import math
class Solution(object):
    def numSquares(self, n):
        # if n==1:
        #     return 1
        if n>0:
          
            x=int(math.sqrt(n))
            m = [float('inf')] * (n + 1)
            m[0]=0
            for i in range(n+1):
                for j in range(x+1):
                    k=j*j
                    if i>=k:
                        m[i]=min(m[i],1+m[i-k])
        return m[n]
        