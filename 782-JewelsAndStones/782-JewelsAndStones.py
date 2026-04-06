# Last updated: 4/6/2026, 10:27:58 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x=list(jewels)
        y=list(stones)
        c=0
        res=[]
        for i in x :
            if i not in res:
                c+=y.count(i)
                res.append(i)
        return c
            



        