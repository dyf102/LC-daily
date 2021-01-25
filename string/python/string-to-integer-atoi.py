class Solution:
    def myAtoi(self, s: str) -> int:
        """LC 8 String to Integer
        """
        result = 0
        is_negative = False
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i == len(s):
            return 0
        if s[i] == '-':
            is_negative = True
            i += 1
        elif s[i] == '+':
            i += 1
        elif not s[i].isdigit():
            return 0
        while i < len(s) and s[i].isdigit():
            result *= 10
            result += (ord(s[i]) - ord('0'))
            i += 1
        if is_negative:
            result *= -1
        if result < -(2**31):
            result = -(2**31)
        elif result > (2**31 - 1):
            result = 2**31 - 1
        return result