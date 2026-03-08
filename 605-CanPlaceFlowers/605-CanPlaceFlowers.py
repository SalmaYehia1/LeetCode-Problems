# Last updated: 3/8/2026, 3:16:13 PM
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        k=len(flowerbed)
        if n==0:
            return True

        if len(flowerbed)==1 and n==1:
            if flowerbed[0]==0:
                return True
            else:
                return False 
        
        i=1
        flowerbed = [0] + flowerbed + [0]

        while i<=k:
                
            if flowerbed[i]==1:
                i+=2
                
            else:
                if flowerbed[i+1]==0 and flowerbed[i-1]==0:
                    flowerbed[i]=1
                    n-=1
                    i+=2
                elif flowerbed[i+1]==1:
                    i+=3
                elif flowerbed[i-1]==1:
                    i+=1
                
         
        if n<=0:
            return True
        else:
            return False 

       
        