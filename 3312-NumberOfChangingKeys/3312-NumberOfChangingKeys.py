# Last updated: 4/6/2026, 10:26:32 PM
class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=s.lower()
        
        c=0
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                c+=1

        return c