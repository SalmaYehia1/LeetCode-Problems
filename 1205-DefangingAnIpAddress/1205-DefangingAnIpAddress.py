# Last updated: 4/6/2026, 10:27:52 PM
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
        