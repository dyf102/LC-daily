class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m == 0:
            return n
        elif n == 0:
            return m
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # base case
        for i in range(1, m + 1):
            dp[i][0] = i
        for i in range(1, n + 1):
            dp[0][i] = i
        
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j] 
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
        return dp[-1][-1]