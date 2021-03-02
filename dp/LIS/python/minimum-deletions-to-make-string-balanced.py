class Solution:
    def minimumDeletions(self, s: str) -> int:
        """LC 1653. Minimum Deletions to Make String Balanced
        Time complexity: O(N)
        t0 means the longest pattern string ending with 'a'
        t1 means the longest pattern string ending with 'b'
        """
        t0 = t1 = 0
        for c in s:
            n0, n1 = t0, t1 
            if c == 'a':
                n0 = t0 + 1
            else:
                n1 = max(t0, t1) + 1
            t0, t1 = n0, n1
        return len(s) - max(t0, t1)