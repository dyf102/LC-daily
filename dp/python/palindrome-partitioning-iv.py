class Solution:
    def checkPartitioning(self, s: str) -> bool:
        """LC 1745. Palindrome Partitioning IV
        Time complexity: O(N^2)
        Args:
            s (str): [description]

        Returns:
            bool: [description]
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            for j in range(i)[::-1]:
                if s[i] == s[j] and (j + 1 == i or dp[j + 1][i - 1]):
                    dp[j][i] = True
        for i in range(n):
            if dp[i][n - 1]:
                for j in range(i - 1):
                    if dp[0][j] and dp[j + 1][i - 1]:
                        return True
        return False