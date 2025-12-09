# Last updated: 12/9/2025, 5:28:13 PM
1class Solution(object):
2    def minPathSum(self, grid):
3
4        m=len(grid)
5        n=len(grid[0])
6
7        dp=[[float('inf') for _ in range(n+1)] for _ in range(m+1)]
8        dp[m-1][n-1] = grid[m-1][n-1]
9
10        for i in range(m-1,-1,-1):
11            for j in range(n-1,-1,-1):
12                
13                if i < m-1:  # can go down
14                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i+1][j])
15                if j < n-1:  # can go right
16                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i][j+1])
17        return dp[0][0]
18      
19        