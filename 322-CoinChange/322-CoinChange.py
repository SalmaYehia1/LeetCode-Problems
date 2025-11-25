# Last updated: 11/25/2025, 5:01:47 PM
class Solution(object):
    def coinChange(self, coins, amount):
        n=len(coins)
        m=[0]*(amount+1)
        for i in range(1,amount+1):
            m[i]=float('inf')
            for coin in coins:
                if (coin<=i):
                    m[i]=min(m[i],1+m[i-coin])
        if m[amount] != float('inf'):
            return m[amount]
        else:
            return -1

