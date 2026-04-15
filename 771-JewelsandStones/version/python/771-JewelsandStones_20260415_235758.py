# Last updated: 4/15/2026, 11:57:58 PM
1class Solution:
2    def numJewelsInStones(self, jewels: str, stones: str) -> int:
3        c=0
4        for i in jewels:
5            if i in stones:
6                c+=stones.count(i)
7    
8        return c 
9        