# Last updated: 3/21/2026, 1:17:04 PM
1class Solution:
2    def theMaximumAchievableX(self, num: int, t: int) -> int:
3        for i in range(t):
4            num+=1
5        num+=t
6        return num
7
8        