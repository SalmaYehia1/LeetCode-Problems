# Last updated: 11/25/2025, 5:01:53 PM
class Solution(object):
    def maxProfit(self, prices):
        q=0
        k=prices[0]

        n=len(prices)
        if n==0 or n==1:
            return 0
        dp=[-1]*n
        for i in range(1,n):
            if prices[i]<k:
                k=prices[i]
            q=prices[i]-k
            dp[i]=max(dp[i],q)
        return max(dp)
                    


       
        