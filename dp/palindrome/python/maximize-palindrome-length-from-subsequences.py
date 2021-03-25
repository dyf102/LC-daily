class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        """LC 1771. Maximize Palindrome Length From Subsequences
        Similar to LC 516 but it adds extra constrains.
        Args:
            word1 (str): [description]
            word2 (str): [description]

        Returns:
            int: [description]
        """
        m = len(word1)
        n = len(word2)
        word = word1 + word2
        c = m + n
        dp = [[0] * c for _ in range(c)]
        for i in range(c):
            dp[i][i] = 1
            for j in range(i)[::-1]: # careful
                if word[j] == word[i]:
                    if j + 1 == i:
                        dp[j][i] = 2 
                    elif j + 2 == i:
                        dp[j][i] = 3
                    else:
                        dp[j][i] = dp[j + 1][i - 1] + 2
                else:
                    dp[j][i] = max(dp[j][i - 1], dp[j + 1][i])
        result = 0
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]: # constrain
                    result = max(result, dp[i][m + j])
        return result