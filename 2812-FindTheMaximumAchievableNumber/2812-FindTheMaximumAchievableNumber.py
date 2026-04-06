# Last updated: 4/6/2026, 10:26:37 PM
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        for i in range(t):
            num+=1
        num+=t
        return num

        