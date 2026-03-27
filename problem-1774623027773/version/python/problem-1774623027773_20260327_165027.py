# Last updated: 3/27/2026, 4:50:27 PM
1class Solution:
2    def reverseDegree(self, s: str) -> int:
3        res = 0
4        for i, ch in enumerate(s):
5            value = ord('z') - ord(ch) + 1
6            res += value * (i + 1)
7        return res