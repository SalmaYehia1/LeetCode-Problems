# Last updated: 2/20/2026, 1:45:08 AM
1class Solution(object):
2    def uniqueOccurrences(self, arr):
3        x=set(arr)
4        
5        res=[]
6        for i in x:
7            res.append(arr.count((i)))
8        res1=set(res)
9
10        if len(res)-2==len(res1) or len(res)==len(res1):
11            return True
12        else:
13            return False
14
15        