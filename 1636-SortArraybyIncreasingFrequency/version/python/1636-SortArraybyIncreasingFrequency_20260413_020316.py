# Last updated: 4/13/2026, 2:03:16 AM
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        temp = []
        for num in freq:
            temp.append([freq[num],num])
        temp.sort(key = lambda x:x[1], reverse = True)
        temp.sort(key = lambda x:x[0])
        ans = []
        for i in temp:
            ans.extend([i[1]]*i[0])
        return ans