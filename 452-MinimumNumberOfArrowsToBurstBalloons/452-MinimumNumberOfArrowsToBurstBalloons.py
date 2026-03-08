# Last updated: 3/8/2026, 3:16:15 PM
class Solution(object):
    def findMinArrowShots(self, points):
        points.sort()
        c=len(points)
        prev=points[0]
        for i in range(1,len(points)):
            curr=points[i]
            if curr[0] <=prev[1]:
                c-=1
                prev=[curr[0],min(curr[1],prev[1])]
            else:
                prev=curr

        return c
                



    # def findMinArrowShots(self, points):
    #     points.sort()
    #     c=1
    #     limit=points[0][1]
    #     for point in points:
    #         if point[0]>limit:
    #             c+=1
    #             limit=point[1]
    #         else:
    #             limit=min(limit,point[1])

    #     return c


        

        
        