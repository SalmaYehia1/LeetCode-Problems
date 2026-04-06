# Last updated: 4/6/2026, 10:28:22 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]