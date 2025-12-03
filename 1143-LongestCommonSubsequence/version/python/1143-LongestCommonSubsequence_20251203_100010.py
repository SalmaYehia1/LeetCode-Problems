# Last updated: 12/3/2025, 10:00:10 AM
1class Solution(object):
2    def longestCommonSubsequence(self, text1, text2):
3        n=len(text2)#cols
4        m=len(text1) #rows
5        dp=[[0 for i in range(n+1)]for j in range(m+1)]
6
7        for i in range(m-1,-1,-1):
8            for j in range(n-1,-1,-1):
9                if text1[i]==text2[j]:
10                    dp[i][j]=1+dp[i+1][j+1]
11                else:
12                    dp[i][j]=max(dp[i][j]+dp[i+1][j],dp[i][j]+dp[i][j+1])
13        return dp[0][0]
14
15
16
17        