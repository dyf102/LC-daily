class Solution:
    def longestPalindrome(self, s: str) -> str:
        """LC 5 Longest Palindromic Substring
        Time complexity: O(N)
        Space: O(N^2)
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True
        start = end = 0
        
        for i in range(1, n):
            dp[i][i] = True
            for j in range(i)[::-1]:
                if s[i] == s[j] and (i == (j + 1) or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j > end - start:
                        start = j
                        end = i
        return s[start: end + 1]