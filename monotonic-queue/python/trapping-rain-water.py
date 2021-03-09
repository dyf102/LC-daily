class Solution:
    def trap(self, height: List[int]) -> int:
        """LC 42. Trapping Rain Water
        Time complexity: O(N)
        """
        queue = []
        i = 0
        n = len(height)
        if n < 1:
            return 0
        queue.append(0)
        i += 1
        result = 0
        while i < n:
            if len(queue) == 0 or height[i] < height[queue[-1]]:
                queue.append(i) 
                i += 1
            else:
                prev = queue.pop()
                if len(queue) > 0:
                    result += (min(height[i], height[queue[-1]]) - height[prev]) * (i - queue[-1] - 1)
            
        return result