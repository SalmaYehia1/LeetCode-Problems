# Last updated: 12/2/2025, 11:36:07 PM
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0 for _ in range(n+1)] for _ in range(m)]

        for i in range(m):
            dp[i][n]=0

        for i in range(n+1):
            dp[m-1][i]=1
        
        for i in range(m-2,-1,-1):
            for j in range(n-1,-1,-1):
                if j<n:
                    dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]      