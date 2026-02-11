# Last updated: 2/11/2026, 4:56:57 PM
1class Solution(object):
2    def mergeAlternately(self, word1, word2):
3        n1=len(word1)
4        n2=len(word2)
5        res=''
6        if n1>n2:
7            for i in range(n1):
8                    if i<n2:
9                        res+=word1[i]
10                        res+=word2[i]
11                    else:
12                        res+=word1[i]
13
14        else:
15            for j in range(n2):
16                    if j<n1:
17                        res+=word1[j]
18                        res+=word2[j]
19                    else:
20                        res+=word2[j]
21        return res
22
23
24       
25
26        
27
28       
29        