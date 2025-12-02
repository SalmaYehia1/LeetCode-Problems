# Last updated: 12/2/2025, 11:37:53 PM
1class Solution(object):
2    def climbStairs(self, n):
3        dp=[0]*(n+1)
4        dp[0]=1
5       
6        for i in range(1,n+1):
7            dp[i]=dp[i-1]+dp[i-2]
8        return dp[n]
9
10#or using 2 variables:
11#x,y=1,1
12# for i in range(n-1):
13#     temp=x
14#     x=x+y
15#     y=temp
16# return x 
17
18
19
20       
21        