# Last updated: 3/8/2026, 3:16:00 PM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        n1=len(word1)
        n2=len(word2)
        res=''
        if n1>n2:
            for i in range(n1):
                    if i<n2:
                        res+=word1[i]
                        res+=word2[i]
                    else:
                        res+=word1[i]

        else:
            for j in range(n2):
                    if j<n1:
                        res+=word1[j]
                        res+=word2[j]
                    else:
                        res+=word2[j]
        return res


       

        

       
        