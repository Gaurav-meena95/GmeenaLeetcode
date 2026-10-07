class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        ans = 0
        for i in range(len(intervals)):
            for j in range(i+ 1,len(intervals)):
                if intervals[i][0] <= intervals[j][1] and  intervals[i][1] >= intervals[j][0]:
                    ans += 1
        return ans
            
            
        