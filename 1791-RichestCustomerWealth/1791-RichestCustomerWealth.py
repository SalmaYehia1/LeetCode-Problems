# Last updated: 4/6/2026, 10:27:02 PM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        c=[]
        for k in accounts:
            c.append(sum(k))
        return max(c)

        