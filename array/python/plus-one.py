class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """LC 66. Plus One

        Args:
            digits (List[int]): [description]

        Returns:
            List[int]: [description]
        """
        carry = 1
        n = len(digits)
        for i in range(n)[::-1]:
            next_carry = (digits[i] + carry) // 10
            digits[i] = (digits[i] + carry) % 10
            carry = next_carry
        
        if carry > 0:
            digits.insert(0, 1)
        return digits