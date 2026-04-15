# Last updated: 4/16/2026, 12:20:23 AM
1from collections import Counter
2class Solution:
3    def findLucky(self, arr: List[int]) -> int:
4        z=Counter(arr)
5        c=[-1]
6        for i in z:
7            if z[i]==i:
8                c+=[i]
9        return max(c)
10        
11
12        