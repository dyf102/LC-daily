class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """LC 200 Number of Islands
        N: num of edge
        M: num of node
        Complexity: O(N + M)
        Args:
            grid (List[List[str]]): [description]

        Returns:
            int: [description]
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        check = [[False] * n for _ in range(m)]
        res = 0
        def dfs(x, y):
            check[x][y] = True
            direction = [0, 1, 0, -1, 0]
            for i in range(4):
                next_x = x + direction[i]
                next_y = y + direction[i + 1]
                if  0 <= next_x < m and 0 <= next_y < n and not check[next_x][next_y] and grid[next_x][next_y] == '1':
                    dfs(next_x, next_y)
                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not check[i][j]:
                    res += 1
                    dfs(i, j)
        return res