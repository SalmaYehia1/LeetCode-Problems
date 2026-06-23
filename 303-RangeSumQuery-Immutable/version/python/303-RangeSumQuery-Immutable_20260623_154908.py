# Last updated: 6/23/2026, 3:49:08 PM
1class NumArray:
2
3    def __init__(self, nums: List[int]):
4        n=len(nums)
5        self.arr=[0]*(n+1)
6        for i in range(n):
7            self.arr[i+1]=nums[i]+ self.arr[i]
8        
9
10    def sumRange(self, left: int, right: int) -> int:
11        return self.arr[right+1]-self.arr[left]
12
13
14