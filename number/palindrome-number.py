import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """LC 9. Palindrome Number
        Time/Sapce complexity: O(1)
        """
        if x == 0:
            return True
        elif x < 0:
            return False
        l = int(math.log(x, 10))
        i = 0
        
        while i <= (l // 2):
            if (x // (10 ** i)) % 10 != ((x // (10 ** (l - i))) % 10):
                return False
            i += 1
        return True