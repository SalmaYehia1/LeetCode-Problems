# Last updated: 4/13/2026, 2:30:11 AM
1from collections import Counter
2class Solution:
3    def mostFrequentEven(self, nums: List[int]) -> int:
4        res=[]
5        for i in nums:
6            if i%2==0:
7                res+=[i]
8        if len(res) == 0:
9            return -1
10        y=Counter(res)
11        y=sorted(y.items() , key =lambda item:( item[1] ,-item[0]),reverse=True)
12        return y[0][0]
13        
14
15        