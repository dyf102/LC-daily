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

    def longestValidParentheses2(self, s: str) -> int:
        """Greedy approach
        """
        n = len(s)
        if n == 0:
            return 0
        left = right = 0
        longest = 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
                if right > left:
                    left = right = 0
            if left == right:
                longest = max(longest, left + right)
        left = right = 0
        for i in range(n)[::-1]:
            if s[i] == ')':
                left += 1
            else:
                right += 1
                if right > left:
                    left = right = 0 # reset
            if left == right:
                longest = max(longest,  left + right)
        return longest