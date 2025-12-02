# Last updated: 12/2/2025, 11:04:18 PM
1class Solution(object):
2    def uniquePaths(self, m, n):
3        dp = [[0 for _ in range(n+1)] for _ in range(m)]
4
5        for i in range(m):
6            dp[i][n]=0
7
8        for i in range(n+1):
9            dp[m-1][i]=1
10        
11        for i in range(m-2,-1,-1):
12            for j in range(n-1,-1,-1):
13                if j<n:
14                    dp[i][j]=dp[i+1][j]+dp[i][j+1]
15        return dp[0][0]      