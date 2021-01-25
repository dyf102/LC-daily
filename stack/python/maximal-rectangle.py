class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """LC 85. Maximal Rectangle
        Submatrix series
        Time Complexity: O(M*N)
        Space: O(N)
        Use a monotonic stack to keep track a increasing sequence.
        Similar questions:
        84. Largest Rectangle in Histogram
        1727. Largest Submatrix With Rearrangements
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        heights = [0] * (n + 1) # deal with items in the stack
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            stack = []
            j = 0
            while j < n + 1:
                if len(stack) == 0 or heights[j] > heights[stack[-1]]:
                    stack.append(j)
                    j += 1
                else:
                    idx = stack.pop()
                    current = heights[idx]
                    if len(stack) == 0:
                        area = current * j
                    else:
                        area = current * (j - stack[-1] - 1)
                    max_area = max(max_area, area)
        return max_area