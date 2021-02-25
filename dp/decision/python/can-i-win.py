class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """LC 464. Can I Win
        top-down approach
        it uses available of left integers as the status
        """
        if desiredTotal == 0:
            return True
        # unfeasible 
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        available = 0
        
        def dp(v, available, cache):
            if available in cache:
                return cache[available]
            if  v <= 0:
                return False
            for i in range(1, maxChoosableInteger + 1):
                if available & (1 << i) == 0 and not dp(v - i, available | (1 << i), cache):
                    cache[available] = True
                    return True
            cache[available] = False
            return False
        return dp(desiredTotal, 0, {})
        