# Last updated: 2/19/2026, 9:52:02 PM
1class Solution(object):
2    def hasAlternatingBits(self, n):
3        
4        binary = bin(n)[2:]
5        k=binary[0]
6        j=0
7        for i in range(1,len(binary)):
8            if k!=binary[i]:
9                k=binary[i]
10                j+=1
11            else:
12                return False
13        if j==len(binary)-1:
14            return True
15        else:
16            return False
17            
18
19
20
21        
22        