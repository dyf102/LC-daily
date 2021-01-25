class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """LC 44. Wildcard Matching
        Time complexity: O(M * N)
        Space: O(N * N)
        Top-botoom approach
        Dp[i][j] means whether s[i:] and p[j:] can be matched
        """
        @lru_cache
        def match(i, j):
            if j == len(p):
                return i == len(s)
            if i == len(s):
                return all([p[k] == '*' for k in range(j, len(p))])
            first_match = (p[j] in (s[i], '?'))
            if p[j] == '*':
                ans = match(i, j + 1) or match(i + 1, j)
            else:
                ans = first_match & match(i + 1, j + 1)
            return ans
        return match(0, 0)

    def isMatch(self, s: str, p: str) -> bool:
        """Bottom-up approach
        """
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        for i in range(n)[::-1]:
            if p[i] != '*':
                break
            dp[m][i] = True
        
        dp[m][n] = True
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                if p[j] in (s[i], '?'):
                    dp[i][j] = dp[i + 1][j + 1]
                elif p[j] == "*":
                    dp[i][j] = dp[i + 1][j] or dp[i][j + 1]
        return dp[0][0]