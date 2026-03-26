# Last updated: 3/26/2026, 2:16:42 PM
1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        res=[]
4        for i in range(n):
5            res.append(nums[i])
6            res.append(nums[i+n])
7        return res
8        