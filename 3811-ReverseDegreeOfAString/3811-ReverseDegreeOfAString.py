# Last updated: 4/6/2026, 10:26:23 PM
class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i, ch in enumerate(s):
            value = ord('z') - ord(ch) + 1
            res += value * (i + 1)
        return res