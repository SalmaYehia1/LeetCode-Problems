# Last updated: 11/25/2025, 5:01:52 PM
class Solution(object):
    def reverseBits(self, b):
        if isinstance(b, int):
            b = format(b, '032b')

        if len(b) == 2:
            return b[::-1]

        mid = len(b) // 2
        left = b[:mid]
        right = b[mid:]

        left_reversed = self.reverseBits(left)
        right_reversed = self.reverseBits(right)

        combined = right_reversed + left_reversed

        if len(combined) == 32:
            return int(combined, 2)

        return combined
