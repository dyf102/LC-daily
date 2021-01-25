import functools

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """LC 1288. Remove Covered Intervals
        Time complexity: O(N*Log(N))
        Space: O(N)
        """
        n = len(intervals)
        def cmp(a, b):
            if a[0] == b[0]:
                return b[1] - a[1]
            else:
                return a[0] - b[0]
        
        intervals.sort(key=functools.cmp_to_key(cmp))
        result = [intervals[0]]
        for i in range(1, n):
            if intervals[i][1] <= result[-1][1]:
                continue
            else:
                result.append(intervals[i])
        return len(result)