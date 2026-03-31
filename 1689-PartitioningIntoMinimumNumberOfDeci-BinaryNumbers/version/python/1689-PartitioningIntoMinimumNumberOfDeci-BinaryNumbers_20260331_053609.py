# Last updated: 3/31/2026, 5:36:09 AM
class Solution:
    def minPartitions(self, n: str) -> int:
        s = set(n)
        s1 = {int(c) for c in s}
        mx = 1
        for c in s1:
            mx = max(mx, c)
        return mx