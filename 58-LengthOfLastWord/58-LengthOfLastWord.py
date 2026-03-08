# Last updated: 3/8/2026, 3:16:32 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split()
        return len(words[-1])
        
        