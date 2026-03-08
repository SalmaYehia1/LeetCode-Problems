# Last updated: 3/8/2026, 3:16:30 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="".join(map(str, digits))
        # result = "".join(map(str, digits))+1
        n=str(int(s)+1)
        res=[]
        for i in range (len(n)):
            res.append(int(n[i]))
        return res