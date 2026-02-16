# Last updated: 2/16/2026, 3:03:56 PM
1class Solution(object):
2    def reverseBits(self, n):
3        bits = format(n, '032b')
4        
5        bits_list = list(bits)
6        
7        bits_list.reverse()
8        
9        res = "".join(bits_list)
10        return int(res, 2)