class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """LC 29. Divide Two Integers
        dividend = divisor * (100010011)
        we need find the binary factor.
        """
        if dividend == 0:
            return 0
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        is_negative = False
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        elif divisor < 0:
            is_negative = True
            divisor = -divisor
        elif dividend < 0:
            is_negative = True
            dividend = -dividend
        result = 0
        while dividend >= divisor:
            for i in range(32):
                if dividend >= divisor * (1 << i):
                    dividend -= divisor * (1 << i)
                    result += (1 << i)
        return result if not is_negative else -result
            