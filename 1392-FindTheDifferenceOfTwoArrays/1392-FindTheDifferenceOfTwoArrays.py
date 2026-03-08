# Last updated: 3/8/2026, 3:16:04 PM
class Solution(object):
    def findDifference(self, nums1, nums2):
        nums_1=set(nums1)
        nums_2=set(nums2)

        l=[]
        m=[]
        for i in nums_1:
            if i not in nums_2:
                l.append(i)

        for j in nums_2:
            if j not in nums_1:
                m.append(j)
        return l,m


       
        