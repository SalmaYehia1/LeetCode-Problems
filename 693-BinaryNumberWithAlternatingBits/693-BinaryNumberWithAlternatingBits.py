# Last updated: 3/8/2026, 3:16:11 PM
class Solution(object):
    def hasAlternatingBits(self, n):
        
        binary = bin(n)[2:]
        k=binary[0]
        j=0
        for i in range(1,len(binary)):
            if k!=binary[i]:
                k=binary[i]
                j+=1
            else:
                return False
        if j==len(binary)-1:
            return True
        else:
            return False
            



        
        