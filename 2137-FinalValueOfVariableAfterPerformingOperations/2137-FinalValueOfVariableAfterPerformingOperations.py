# Last updated: 4/6/2026, 10:26:43 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for k in operations:
            if k[1]=="+":
                x+=1
            else:
                x-=1
        return x

        