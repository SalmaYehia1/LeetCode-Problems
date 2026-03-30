# Last updated: 3/31/2026, 1:12:42 AM
1class Solution:
2    def mostWordsFound(self, sentences: List[str]) -> int:
3        k = 0
4        for i in sentences:
5            l = len(i.split())  
6            if l >= k:
7                k = l           
8        return k