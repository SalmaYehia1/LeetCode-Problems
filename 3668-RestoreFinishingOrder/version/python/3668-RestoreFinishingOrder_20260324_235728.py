# Last updated: 3/24/2026, 11:57:28 PM
1class Solution:
2    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
3        res=[]
4        for k in order:
5            if k in friends:
6                res.append(k)
7        return res
8
9        