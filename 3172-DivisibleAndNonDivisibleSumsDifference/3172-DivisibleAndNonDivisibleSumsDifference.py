# Last updated: 4/6/2026, 10:26:35 PM
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k=0
        c=0
        for i in range(n+1):
            if i%m==0:
                c+=i
            else:
                k+=i
        return k-c

        