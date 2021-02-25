class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """LC 240. Search a 2D Matrix II
        Time complexity: O(M + N)
        """
        m = len(matrix)
        n = len(matrix[0])
        x, y = m -1, 0
        while x >= 0 and y < n:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                x -= 1
            else:
                y += 1
        return False