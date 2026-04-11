# Last updated: 4/11/2026, 1:29:55 PM
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3        arr = [abs(x) for x in nums]
4        arr.sort()
5        k=[]
6        for i in arr:
7            k.append(i*i)
8        return k
9
10        