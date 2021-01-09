class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        """LC 1706 Where Will the Ball Fall 
        Difficuty: Medium
        Time complexity: O(N)
        Space: O(1)
        Args:
            grid (List[List[int]]): [description]

        Returns:
            List[int]: [description]
        """
        m = len(grid)
        n = len(grid[0])
        result = [-1] * n
        
        for i in range(n):
            left = i
               
            for j in range(m):
                right = left + grid[j][left]
                if right < 0 or right >= n or grid[j][left] != grid[j][right]: 
                    break
                left = right 
                if j == m -1: # fall into last row
                    result[i] = left
        return result