# Last updated: 12/4/2025, 5:21:49 AM
1class Solution(object):
2    def findMinArrowShots(self, points):
3        points.sort()
4        c=len(points)
5        prev=points[0]
6        for i in range(1,len(points)):
7            curr=points[i]
8            if curr[0] <=prev[1]:
9                c-=1
10                prev=[curr[0],min(curr[1],prev[1])]
11            else:
12                prev=curr
13
14        return c
15                
16
17
18
19    # def findMinArrowShots(self, points):
20    #     points.sort()
21    #     c=1
22    #     limit=points[0][1]
23    #     for point in points:
24    #         if point[0]>limit:
25    #             c+=1
26    #             limit=point[1]
27    #         else:
28    #             limit=min(limit,point[1])
29
30    #     return c
31
32
33        
34
35        
36        