class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """LC 1143. Longest Common Subsequence

        Args:
            text1 (str): [description]
            text2 (str): [description]

        Returns:
            int: length of LCS
        """
        m = len(text1)
        n = len(text2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]