from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """LC 329 Longest Increasing Path in a Matrix
        time complexity: O(M * N)
        space: O(E)
        BFS according to topological order
        """
        m = len(matrix)
        n = len(matrix[0])
        indegree = [[0] * n for _ in range(m)]
        direction = [0, 1, 0, -1, 0]
        queue = deque()
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                for k in range(4):
                    next_x = i + direction[k]
                    next_y = j + direction[k + 1]
                    if 0 <= next_x < m and 0 <= next_y < n and matrix[next_x][next_y] > val:
                        indegree[next_x][next_y] += 1
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    queue.append((i, j))
        
        res = 0
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                val = matrix[x][y]
                for k in range(4):
                    next_x = x + direction[k]
                    next_y = y + direction[k + 1]
                    if 0 <= next_x < m and 0 <= next_y < n and matrix[next_x][next_y] > val:
                        indegree[next_x][next_y] -= 1
                        if indegree[next_x][next_y] == 0:
                            queue.append((next_x, next_y))
            res += 1
        return res
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """DFS + memorization 
        Top-down approach
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        def dfs(x, y):
            if dp[x][y] != -1:
                return dp[x][y]
            direction = [0, 1, 0, -1, 0]
            val = matrix[x][y]
            curr = 1
            for i in range(4):
                next_x = x + direction[i]
                next_y = y + direction[i + 1]
                if 0 <= next_x < m and 0 <= next_y < n  and matrix[next_x][next_y] > val:
                    curr = max(curr, dfs(next_x, next_y) + 1)
            dp[x][y] = curr
            return curr
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """Bottom-up approach
        Since it's increasing sequence, we start from largest cell and iterate backward. 
        """
        m = len(matrix)
        n = len(matrix[0])
        if m == 0: return 0
        dp = [[1] * n for _ in range(m)]
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((matrix[i][j], i , j))
        cells.sort(reverse=True)
        res = 1
        direction = [0, 1, 0, -1, 0]
        for val, x, y in cells[1:]:
            curr = 1
            for i in range(4):
                next_x = x + direction[i]
                next_y = y + direction[i + 1]
                if 0 <= next_x < m and 0 <= next_y < n and matrix[next_x][next_y] > val:
                    curr = max(curr, dp[next_x][next_y] + 1)
            dp[x][y] = curr
            res = max(curr, res)
        return res
