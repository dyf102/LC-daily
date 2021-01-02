class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """LC 695 Max Area of Island
        Time Complexity: O(N)
        Space: O(N)
        Union-find
        Args:
            grid (List[List[int]]): [description]

        Returns:
            int: [description]
        """
        m = len(grid)
        n = len(grid[0])
        parent = [i for i in range(m*n)]
        rank = [0] * (m*n)
        size = [1] * (m*n)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            if p_x != p_y:
                if rank[p_x] > rank[p_y]:
                    parent[p_y] = p_x
                    size[p_x] += size[p_y]
                    return size[p_x]
                else:
                    parent[p_x] = p_y
                    if rank[p_x] == rank[p_y]:
                        rank[p_y] += + 1
                    size[p_y] += size[p_x]
                    return size[p_y]
            return size[p_x]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                res = max(1, res)
                current = j + i * n
                direction = [0, 1, 0, -1, 0]
                for k in range(4):
                    next_x = i + direction[k]
                    next_y = j + direction[k + 1]
                    if  0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1:
                        next_idx = next_x * n + next_y
                        res = max(res, union(current, next_idx))
        return res
                