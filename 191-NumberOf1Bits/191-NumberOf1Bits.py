# Last updated: 4/6/2026, 10:28:14 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]
        c=0
        for i in range(len(b)):
            if b[i]=='1':
                c+=1
        return c

        