# Last updated: 4/6/2026, 10:27:05 PM
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1="".join(word1)
        s2="".join(word2)
        if s1==s2:
            return True
        else:
            return False