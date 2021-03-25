class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """LC 63. Unique Paths II
        Be careful about corner cases
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        if obstacleGrid[0][0] != 1:
            dp[1][1] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i + 1][j + 1] += dp[i + 1][j] + dp[i][j + 1]
        return dp[-1][-1]