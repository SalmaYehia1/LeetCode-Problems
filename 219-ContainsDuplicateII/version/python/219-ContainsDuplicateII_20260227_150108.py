# Last updated: 2/27/2026, 3:01:08 PM
1
2class Solution(object):
3    def containsNearbyDuplicate(self, nums, k):
4        x=set(nums)
5        if len(x)==len(nums):
6            return False
7        else:
8            for i in range(len(nums)):
9                for j in range(i+1,len(nums)):
10                    if nums[i]==nums[j] and abs(i - j) <= k:
11                        return True
12                    
13            return False
14
15
16        
17            