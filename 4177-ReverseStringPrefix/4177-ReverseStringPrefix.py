# Last updated: 4/6/2026, 10:26:19 PM
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        res=""
        res+=s[k-1::-1]
        res+=s[k:]
        return res
        
        