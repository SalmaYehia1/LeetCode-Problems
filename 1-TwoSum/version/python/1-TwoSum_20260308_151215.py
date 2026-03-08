# Last updated: 3/8/2026, 3:12:15 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        s="".join(map(str, digits))
4        # result = "".join(map(str, digits))+1
5        n=str(int(s)+1)
6        res=[]
7        for i in range (len(n)):
8            res.append(int(n[i]))
9        return res