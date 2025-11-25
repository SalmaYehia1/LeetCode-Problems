# Last updated: 11/25/2025, 5:01:55 PM
class Solution(object):
    def searchMatrix(self, matrix, target):
        
        m = len(matrix)        #rows 
        n = len(matrix[0])     #cols
        row=0
        col=n-1
        while row<m and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            else:
                col-=1
        return False
        
        