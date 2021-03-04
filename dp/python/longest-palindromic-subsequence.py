class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """LC 516. Longest Palindromic Subsequence
        Time complexity: O(N^2)
        """
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for i in range(n):
            for j in range(i)[::-1]:
                if s[i] == s[j]:
                    if i - j <= 2:
                        dp[j][i] = i - j + 1
                    else:
                        dp[j][i] = dp[j + 1][i - 1] + 2
                else:
                    # substring normal pattern
                    dp[j][i] = max(dp[j + 1][i], dp[j][i - 1])
        return dp[0][-1]                        