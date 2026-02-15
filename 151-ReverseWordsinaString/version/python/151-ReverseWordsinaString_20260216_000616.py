# Last updated: 2/16/2026, 12:06:16 AM
1class Solution(object):
2    def reverseWords(self, s):
3        words = s.split()
4        words.reverse()
5        return " ".join(words)
6
7
8        
9        