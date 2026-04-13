# Last updated: 4/13/2026, 2:15:18 AM
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x=zip(heights,names)
        x=sorted(x,reverse=True)
        res=[]
        for h , n in x:
            res.append(n)
        return res


        