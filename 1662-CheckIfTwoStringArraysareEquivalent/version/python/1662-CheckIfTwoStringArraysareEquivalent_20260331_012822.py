# Last updated: 3/31/2026, 1:28:22 AM
1class Solution:
2    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
3        s1="".join(word1)
4        s2="".join(word2)
5        if s1==s2:
6            return True
7        else:
8            return False