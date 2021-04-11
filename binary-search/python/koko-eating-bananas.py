import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """LC 875. Koko Eating Bananas

        Args:
            piles (List[int]): [description]
            h (int): [description]

        Returns:
            int: [description]
        """
        def canFinished(speed):
            need = 0
            for pile in piles:
                need += math.ceil(pile / speed)
                if need > h:
                    return False
            return True
        
        left = 1
        right = 10**9
        while left < right:
            m = (left + right) // 2
            if canFinished(m):
                right = m
            else:
                left = m + 1
        return left