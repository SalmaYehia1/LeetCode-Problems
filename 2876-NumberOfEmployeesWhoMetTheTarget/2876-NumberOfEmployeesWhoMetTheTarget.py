# Last updated: 4/7/2026, 5:20:58 PM
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        if target in hours:
            hours.sort()
            i=hours.index(target)
        else:
            hours.append(target)
            hours.sort()
            i=hours.index(target)+1
            

        
        return len(hours)-i
        