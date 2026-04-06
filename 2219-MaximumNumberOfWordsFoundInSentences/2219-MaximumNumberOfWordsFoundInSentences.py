# Last updated: 4/6/2026, 10:47:55 PM
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        k = 0
        for i in sentences:
            l = len(i.split())  
            if l >= k:
                k = l           
        return k