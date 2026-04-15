# Last updated: 4/16/2026, 12:12:08 AM
1from collections import Counter
2class Solution:
3    def areOccurrencesEqual(self, s: str) -> bool:
4        z=Counter(s)
5        return len(set(z.values())) == 1
6
7        
8        