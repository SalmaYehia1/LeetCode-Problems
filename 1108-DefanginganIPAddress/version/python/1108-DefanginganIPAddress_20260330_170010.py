# Last updated: 3/30/2026, 5:00:10 PM
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
        