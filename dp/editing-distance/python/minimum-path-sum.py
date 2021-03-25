class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """LC 64. Minimum Path Sum
        """
        m = len(grid)
        n = len(grid[0])
        check = [[False] * n for _ in range(m)]
        @lru_cache()
        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return grid[-1][-1]
            
            v = float('inf')
            
            if x + 1 < m and not check[x + 1][y]:
                check[x + 1][y] = True
                v = min(v, dfs(x + 1, y))
                check[x + 1][y] = False
            
            if y + 1 < n and not check[x][y + 1]:
                check[x][y + 1] = True
                v = min(v, dfs(x, y + 1))
                check[x][y + 1] = False
            
            return v + grid[x][y]
        
        return dfs(0, 0)

    def minPathSum2(self, grid: List[List[int]]) -> int:
        """top-down approach
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 0
        
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
        
        return dp[-1][-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [float('inf')] * (n + 1)
        dp[1] = 0
        
        for i in range(m):
            for j in range(n):
                dp[j + 1] = min(dp[j + 1], dp[j]) + grid[i][j]
        
        return dp[-1]
        
        