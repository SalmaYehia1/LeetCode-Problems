# Last updated: 11/25/2025, 5:01:51 PM
class Solution(object):
    def searchMatrix(self, matrix, target):
        
        m = len(matrix)        #rows 
        n = len(matrix[0])     #cols
        row=0
        col=n-1
        while row<m and col>=0:
            x=matrix[row][col]
            if x==target:
                return True
            elif x<target:
                row+=1
            else:
                col-=1
        return False
        
        