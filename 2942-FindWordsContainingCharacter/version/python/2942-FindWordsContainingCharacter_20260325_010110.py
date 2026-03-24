# Last updated: 3/25/2026, 1:01:10 AM
1class Solution:
2    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
3        ans = []
4        
5        for index, k in enumerate(words):
6            if x in k:
7                ans.append(index) 
8                
9        return ans