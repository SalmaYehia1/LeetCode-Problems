# Last updated: 12/4/2025, 5:11:26 AM
1class Solution(object):
2    def findMinArrowShots(self, points):
3        points.sort()
4        c=1
5        limit=points[0][1]
6        for point in points:
7            if point[0]>limit:
8                c+=1
9                limit=point[1]
10            else:
11                limit=min(limit,point[1])
12
13        return c
14
15
16        
17
18        
19        