# Last updated: 4/13/2026, 2:01:58 AM
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = []
        count = collections.defaultdict(int)

        for n in nums:
            count[n] += 1
        for k, v in sorted(count.items(), key=lambda x: (x[1], -x[0])):
            res += [k] * v
        return res