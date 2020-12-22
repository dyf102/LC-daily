class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """LC 1277 
        it's similar to LC 221 
        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

        Args:
            matrix (List[List[int]]): [description]

        Returns:
            int: # of sqaure in the matrix
        """
        m = len(matrix)
        if m < 1:
            return 0
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
                    res += dp[i + 1][j + 1]
        return res