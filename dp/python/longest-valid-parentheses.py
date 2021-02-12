class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """LC 32. Longest Valid Parentheses
        Time complexity: O(N)
        Space: O(N)
        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        """
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i - dp[i - 1] - 1] == '(' and i - dp[i - 1] - 1 >= 0:
                    dp[i] = dp[i - 1] + 2 + 0 if i - dp[i - 1] - 2 == -1 else dp[i - dp[i - 1] - 2]
        # print(dp)
        return max(dp)