# Last updated: 3/20/2026, 3:11:28 AM
1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        return bin(int(a,2)+int(b,2))[2:]