class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """LC 583. Delete Operation for Two Strings

        Args:
            word1 (str): [description]
            word2 (str): [description]

        Returns:
            int: [description]
        """
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(n + 1):
            dp[0][i] = i
        
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i + 1][j] , dp[i][j + 1] ) + 1
        return dp[-1][-1]