# Last updated: 3/8/2026, 3:16:31 PM
class Solution(object):
    def minPathSum(self, grid):

        m=len(grid)
        n=len(grid[0])

        dp=[[float('inf') for _ in range(n+1)] for _ in range(m+1)]
        dp[m-1][n-1] = grid[m-1][n-1]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                
                if i < m-1:  # can go down
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i+1][j])
                if j < n-1:  # can go right
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i][j+1])
        return dp[0][0]
      
        