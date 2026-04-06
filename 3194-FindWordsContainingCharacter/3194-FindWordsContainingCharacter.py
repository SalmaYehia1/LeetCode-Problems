# Last updated: 4/6/2026, 10:26:33 PM
class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        ans = []
        
        for index, k in enumerate(words):
            if x in k:
                ans.append(index) 
                
        return ans