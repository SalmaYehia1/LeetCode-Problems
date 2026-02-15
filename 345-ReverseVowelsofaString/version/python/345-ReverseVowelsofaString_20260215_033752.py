# Last updated: 2/15/2026, 3:37:52 AM
1class Solution(object):
2    def reverseVowels(self, s):
3        k=[]
4        s = list(s)
5        
6        vowels = "aeiouAEIOU"
7        for i in range(len(s)):
8            if s[i] in vowels:
9                k.append(i)
10        for j in range(len(k)//2):
11            temp=s[k[j]]
12            s[k[j]]=s[k[len(k)-1-j]]
13            s[k[len(k)-1-j]]=temp
14        return "".join(s)
15
16
17
18       
19        