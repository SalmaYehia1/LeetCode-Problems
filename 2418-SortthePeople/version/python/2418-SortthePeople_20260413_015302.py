# Last updated: 4/13/2026, 1:53:02 AM
1class Solution:
2    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
3        x=zip(heights,names)
4        x=sorted(x,reverse=True)
5        res=[]
6        for h , n in x:
7            res.append(n)
8        return res
9
10
11        