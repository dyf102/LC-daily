from collections import Counter
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        """LC 356. Line Reflection
        Time complexity: O(N*Log(N))
        Space: O(N)
        """
        n = len(points)
        points.sort(key=lambda x: x[0])
        left = points[0][0]
        right = points[-1][0]
        middle = (left + right) / 2
        i = 0
        count = Counter()
        while i < n:
            if i + 1 < n and points[i] == points[i + 1]: # dedup
                pass
            elif points[i][0] < middle:
                count[(points[i][0],points[i][1])] += 1
            elif points[i][0] > middle:
                prev = (2 * middle - points[i][0], points[i][1])
                count[prev] -= 1
                if count[prev] < 0:
                    return False
            i += 1
        return all([v == 0 for v in count.values()]) # validate leftout