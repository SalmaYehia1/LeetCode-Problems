# Last updated: 2/13/2026, 5:15:47 PM
1class Solution(object):
2    def gcdOfStrings(self, str1, str2):
3        n1=len(str1)
4        n2=len(str2)
5        c=str1+str2
6        b=str2+str1
7        if b==c:
8            n=self.gcd(n1,n2)
9            return str1[0:n]
10        else:
11            return ""        
12        
13
14
15    def gcd(self,x,y):
16        while y:
17            x,y=y,x%y
18        return x
19
20            
21
22      
23        