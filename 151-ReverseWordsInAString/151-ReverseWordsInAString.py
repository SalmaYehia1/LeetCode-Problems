# Last updated: 3/8/2026, 3:16:25 PM
class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words)


        
        