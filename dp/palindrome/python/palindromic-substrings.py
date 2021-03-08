class Solution:
    def countSubstrings(self, s: str) -> int:
        """LC 647. Palindromic Substrings
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        
        for i in range(n):
            dp[i][i] = True
            count += 1
            for j in range(i)[::-1]:
                if s[i] == s[j]:
                    if i - j <= 2:
                        dp[j][i] = True
                        count += 1
                    elif dp[j + 1][i - 1]:
                        dp[j][i] = True
                        count += 1
        return count