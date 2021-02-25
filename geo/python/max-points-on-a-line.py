import math
from collections import Counter

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """LC 149. Max Points on a Line
        Complexity: O(N^2)
        Args:
            points (List[List[int]]): [description]

        Returns:
            int: [description]
        """
        n = len(points)
        if n <= 2:
            return n
        def get_angle(x1, x2, y1, y2):
            diff_x, diff_y = x2 - x1, y2 - y1
            
            if diff_x == 0: # vertical
                return (0, 0)
            elif diff_y == 0: # horizental
                return (float('inf'), float('inf'))
            elif diff_x < 0:
                diff_x, diff_y = -diff_x, -diff_y
            gcd = math.gcd(diff_x, diff_y)
            angle = (diff_y / gcd, diff_x/ gcd)
            return angle

        def colinear(idx):
            x, y = points[idx][0], points[idx][1]
            counter = Counter()
            count = 0
            duplicate = 1
            for i in range(n):
                if i == idx: continue
                x2, y2 = points[i][0], points[i][1]
                if x2 == x and y2 == y:
                    duplicate += 1 # duplicated points
                    continue
                angle = get_angle(x, x2, y, y2)
                counter[angle] += 1
                count = max(count, counter[angle])
            return count + duplicate
        
        result = 2
        for i in range(n):
            result = max(result, colinear(i))
        return result