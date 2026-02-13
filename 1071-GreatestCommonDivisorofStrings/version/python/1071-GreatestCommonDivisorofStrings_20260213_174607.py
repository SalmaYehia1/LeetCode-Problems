# Last updated: 2/13/2026, 5:46:07 PM
1class Solution(object):
2    def kidsWithCandies(self, candies, extraCandies):
3        max1 =max(candies)
4        res=[]
5        for i in range(len(candies)):
6           res.append(candies[i]+extraCandies>=max1)
7        return res
8
9        
10        