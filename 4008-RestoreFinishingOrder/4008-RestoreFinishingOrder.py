# Last updated: 4/6/2026, 10:26:11 PM
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res=[]
        for k in order:
            if k in friends:
                res.append(k)
        return res

        