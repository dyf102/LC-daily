class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left + 1 < right:
            m = (left + right) // 2
            if m**2 > x:
                right = m - 1
            else:
                left = m
        if right <= x and right * right <= x:
            return right
        return left
    
    def mySqrt2(self, x: int) -> int:
        left = 1
        right = x + 1
        while left < right:
            m = (left + right) // 2
            if m**2 > x:
                right = m
            else:
                left = m + 1
        return left - 1