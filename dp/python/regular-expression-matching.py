from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """LC 10. Regular Expression Matching
        Time complexity: O(M + N)
        Space: O(M * N)
        """
        @lru_cache
        def match(i, j):
            if j == len(p):
                return i == len(s)
            first_match = (p[j] in [s[i], '.']) if i < len(s) else False
            if j + 1 < len(p) and p[j + 1] == '*':
                ans = (match(i, j + 2)) or (first_match and match(i + 1, j))
            else:
                ans = first_match and match(i + 1, j + 1)
            return ans
        return match(0, 0)