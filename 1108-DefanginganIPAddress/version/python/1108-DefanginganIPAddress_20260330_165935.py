# Last updated: 3/30/2026, 4:59:35 PM
1class Solution:
2    def defangIPaddr(self, address: str) -> str:
3        res=address.replace(".","[.]")
4        return res