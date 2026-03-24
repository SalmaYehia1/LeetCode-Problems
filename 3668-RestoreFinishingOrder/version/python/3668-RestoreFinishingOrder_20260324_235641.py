# Last updated: 3/24/2026, 11:56:41 PM
1class Solution:
2    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
3        res=[]
4        for i in range(len(order)):
5            if order[i] in friends:
6                res.append(order[i])
7        return res
8
9        