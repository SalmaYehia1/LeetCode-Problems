# Last updated: 4/11/2026, 10:52:29 AM
1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        k=[]
4        c=0
5        for i in nums:
6            c+=i
7            k.append(c)
8        return k
9
10        