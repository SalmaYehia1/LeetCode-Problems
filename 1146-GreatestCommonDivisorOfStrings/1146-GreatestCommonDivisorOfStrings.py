# Last updated: 3/8/2026, 3:16:08 PM
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        n1=len(str1)
        n2=len(str2)
        c=str1+str2
        b=str2+str1
        if b==c:
            n=self.gcd(n1,n2)
            return str1[0:n]
        else:
            return ""        
        


    def gcd(self,x,y):
        while y:
            x,y=y,x%y
        return x

            

      
        