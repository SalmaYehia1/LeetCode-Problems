# Last updated: 4/13/2026, 2:16:26 AM
1from collections import Counter
2
3class Solution:
4    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
5        if len(nums)<=1:
6            return nums
7        x=Counter(nums)
8        x=sorted(x.items(), key=lambda item: item[1],reverse=True)
9        res=[]
10
11        for i , j in x:
12            if len(res)==k:
13                return res
14            else:
15                res+=[i]
16        return res
17
18
19
20
21        