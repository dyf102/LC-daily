class Solution:
    def canWin(self, s: str) -> bool:
        """LC 294. Flip Game II
        """
        cache = {}
        n = len(s)
        @lru_cache()
        def dp(status):
            if '++' not in status:
                return False
            for i in range(n - 1):
                if status[i] == '+' and status[i + 1] == '+':
                    if not dp(status[:i] + "--" + status[i + 2:]):
                        return True
            return False
        return dp(s)