# Last updated: 3/25/2026, 12:07:38 AM
1class Solution:
2    def finalValueAfterOperations(self, operations: List[str]) -> int:
3        x=0
4        for k in operations:
5            if k[1]=="+":
6                x+=1
7            else:
8                x-=1
9        return x
10
11        