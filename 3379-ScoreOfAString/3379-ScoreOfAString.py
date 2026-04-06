# Last updated: 4/6/2026, 10:26:30 PM
class Solution:
    def scoreOfString(self, s: str) -> int:
        k=0
        for i in range(len(s)-1):
            k+=abs(ord(s[i])-ord(s[i+1]))
        return k

        