# Last updated: 3/30/2026, 5:11:01 PM
1class Solution:
2    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
3        allowed_set = set(allowed)
4        count = 0
5
6        for word in words:
7            if all(ch in allowed_set for ch in word):
8                count += 1
9
10        return count