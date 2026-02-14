# Last updated: 2/15/2026, 12:29:40 AM
1class Solution(object):
2    def canPlaceFlowers(self, flowerbed, n):
3        k=len(flowerbed)
4        if n==0:
5            return True
6
7        if len(flowerbed)==1 and n==1:
8            if flowerbed[0]==0:
9                return True
10            else:
11                return False 
12        
13        i=1
14        flowerbed = [0] + flowerbed + [0]
15
16        while i<=k:
17                
18            if flowerbed[i]==1:
19                i+=2
20                
21            else:
22                if flowerbed[i+1]==0 and flowerbed[i-1]==0:
23                    flowerbed[i]=1
24                    n-=1
25                    i+=2
26                elif flowerbed[i+1]==1:
27                    i+=3
28                elif flowerbed[i-1]==1:
29                    i+=1
30                
31         
32        if n<=0:
33            return True
34        else:
35            return False 
36
37       
38        