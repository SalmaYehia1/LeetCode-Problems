# Last updated: 4/13/2026, 2:09:19 AM
1
2from collections import Counter 
3class Solution:
4    def frequencySort(self, s: str) -> str:
5        
6        y=Counter(s)
7        y=sorted(y.items() , key=lambda item:item[1],reverse=True)
8        res=""
9
10        for i , j in y:
11            res+=i*j
12        return res
13
14        
15            