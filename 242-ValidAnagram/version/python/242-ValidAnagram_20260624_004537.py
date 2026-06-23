# Last updated: 6/24/2026, 12:45:37 AM
1from collections import Counter 
2class Solution:
3    def isAnagram(self, s: str, t: str) -> bool:
4       return Counter(s)==Counter(t)
5        