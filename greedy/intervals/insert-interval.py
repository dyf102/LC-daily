class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """LC 57. Insert Interval
        Time complexity: O(N)
        """
        result = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        result.append(newInterval)
        while i < n and intervals[i][0] <= result[-1][1]:
            result[-1][0] = min(result[-1][0], intervals[i][0])
            result[-1][1] = max(intervals[i][1], result[-1][1])
            i += 1
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
        
        