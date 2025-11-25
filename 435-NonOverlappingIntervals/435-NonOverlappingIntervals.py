# Last updated: 11/25/2025, 5:01:48 PM

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        intervals_sorted = sorted(intervals, key=lambda x: x[1])

        c=1
        n=len(intervals)
        finish=intervals_sorted [0][1]
        for i in range(1,n):
            start_i=intervals_sorted [i][0]
            finish_i=intervals_sorted [i][1]
            if start_i>=finish:
                c+=1
                finish=finish_i
    
        return n-c
        
