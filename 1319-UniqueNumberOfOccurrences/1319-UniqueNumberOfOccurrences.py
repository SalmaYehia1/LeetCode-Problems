# Last updated: 3/8/2026, 3:16:03 PM
class Solution(object):
    def uniqueOccurrences(self, arr):
        x=set(arr)
        
        res=[]
        for i in x:
            res.append(arr.count((i)))
        res1=set(res)

        if len(res)==len(res1):
            return True
        else:
            return False

        