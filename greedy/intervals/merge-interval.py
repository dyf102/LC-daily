class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """LC 56. Merge Intervals

        """
        n = len(intervals)
        
        intervals.sort(key=lambda x:x[0])
        
        result = [intervals[0]]
        for i in range(1, n):
            current = intervals[i]
            if current[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], current[1])
            else:
                result.append(current)
        return result