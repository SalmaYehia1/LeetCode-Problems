# Last updated: 3/8/2026, 3:15:59 PM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max1 =max(candies)
        res=[]
        for i in range(len(candies)):
           res.append(candies[i]+extraCandies>=max1)
        return res

        
        