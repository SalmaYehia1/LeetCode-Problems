# Last updated: 3/8/2026, 3:16:16 PM
class Solution(object):
    def reverseVowels(self, s):
        k=[]
        s = list(s)
        
        vowels = "aeiouAEIOU"
        for i in range(len(s)):
            if s[i] in vowels:
                k.append(i)
        for j in range(len(k)//2):
            temp=s[k[j]]
            s[k[j]]=s[k[len(k)-1-j]]
            s[k[len(k)-1-j]]=temp
        return "".join(s)



       
        