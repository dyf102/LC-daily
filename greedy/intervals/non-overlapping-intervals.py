class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """LC 435. Non-overlapping Intervals
        Critical part is it's using end time to sort because 
        we can discord the one ending earlier.
        Args:
            intervals (List[List[int]]): [description]

        Returns:
            int: [description]
        """
        intervals.sort(key=lambda x: x[1])
        count = 0
        last = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[last][1]:
                count += 1
            else:
                last = i
        return count