# Last updated: 4/13/2026, 2:01:20 AM
1from collections import Counter
2class Solution:
3    def frequencySort(self, nums: List[int]) -> List[int]:
4        x=Counter(nums)
5        x =sorted(x.items(), key=lambda item: (item[1], -item[0])) #if there is a tie
6        res=[]
7        print(x)
8        for i , j in x:
9
10            res.extend([i]*j)
11        return res
12
13
14        