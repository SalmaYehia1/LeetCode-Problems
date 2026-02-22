# Last updated: 2/22/2026, 2:18:57 AM
1class Solution(object):
2    def findDifference(self, nums1, nums2):
3        nums_1=set(nums1)
4        nums_2=set(nums2)
5
6        l=[]
7        m=[]
8        for i in nums_1:
9            if i not in nums_2:
10                l.append(i)
11
12        for j in nums_2:
13            if j not in nums_1:
14                m.append(j)
15        return l,m
16
17
18       
19        