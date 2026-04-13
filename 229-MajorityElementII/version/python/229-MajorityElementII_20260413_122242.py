# Last updated: 4/13/2026, 12:22:42 PM
1from collections import Counter
2class Solution:
3    def majorityElement(self, nums: List[int]) -> List[int]:
4        n=len(nums)
5        if n==1:
6            return nums
7        n=n//3
8
9        y=Counter(nums)
10        x=sorted(y.items(),key=lambda item :item[1])
11        res=[]
12        for i,j in x:
13            if j>n:
14                res+=[i]
15        return res
16
17
18        
19        
20        