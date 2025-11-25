# Last updated: 11/25/2025, 5:01:38 PM
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        c=0
        if not boxTypes:
            return 0
        n=len(boxTypes)
        for i  in range(0,n):
            if truckSize>=boxTypes[i][0]:
                c=c+(boxTypes[i][0]*boxTypes[i][1])
                truckSize-=boxTypes[i][0]
            else:
                c=c+(truckSize*boxTypes[i][1])
                truckSize=0

        return c 



        
        
        