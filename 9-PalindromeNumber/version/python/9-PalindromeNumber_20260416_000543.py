# Last updated: 4/16/2026, 12:05:43 AM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if str(x)[::-1]==str(x):
4            return True 
5        else:
6            return False
7        