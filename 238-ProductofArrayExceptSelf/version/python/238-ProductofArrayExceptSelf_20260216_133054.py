# Last updated: 2/16/2026, 1:30:54 PM
1class Solution(object):
2    def productExceptSelf(self, nums):
3        res=[]
4        k=1
5        for m in range(len(nums)):
6            k*=nums[m]
7        
8
9
10        for i in range(len(nums)):
11            s=1
12            if nums[i]==0:
13                for n in range(len(nums)):
14                    
15
16                    if n!=i:
17                        s*=nums[n]
18                res.append(s)
19
20
21            else:
22                res.append(k/nums[i])
23            
24        return res
25
26        
27        