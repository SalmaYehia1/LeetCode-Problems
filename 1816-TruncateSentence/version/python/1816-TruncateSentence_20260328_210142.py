# Last updated: 3/28/2026, 9:01:42 PM
1class Solution:
2    def truncateSentence(self, s: str, k: int) -> str:
3        words = s.split()
4        return " ".join(words[:k])
5        