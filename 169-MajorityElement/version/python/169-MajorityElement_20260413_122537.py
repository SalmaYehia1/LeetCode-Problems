# Last updated: 4/13/2026, 12:25:37 PM
1from collections import Counter
2class Solution:
3    def majorityElement(self, nums: List[int]) -> List[int]:
4        n=len(nums)
5        if n==1:
6            return nums[0]
7        n=n//2
8
9        y=Counter(nums)
10        x=sorted(y.items(),key=lambda item :item[1])
11        res=[]
12        for i,j in x:
13            if j>n:
14                return i
15
16
17        
18        
19        