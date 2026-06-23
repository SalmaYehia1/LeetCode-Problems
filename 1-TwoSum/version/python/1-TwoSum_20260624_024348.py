# Last updated: 6/24/2026, 2:43:48 AM
1from collections import Counter
2class Solution:
3    def majorityElement(self, nums: List[int]) -> List[int]:
4        c=Counter(nums)
5        return c.most_common(1)[0][0]
6        
7        