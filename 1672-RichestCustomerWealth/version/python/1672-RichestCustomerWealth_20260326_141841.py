# Last updated: 3/26/2026, 2:18:41 PM
1class Solution:
2    def maximumWealth(self, accounts: List[List[int]]) -> int:
3        c=[]
4        for k in accounts:
5            c.append(sum(k))
6        return max(c)
7
8        