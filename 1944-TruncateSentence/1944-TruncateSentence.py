# Last updated: 4/6/2026, 10:26:49 PM
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        return " ".join(words[:k])
        