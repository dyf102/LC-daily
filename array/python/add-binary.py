class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """LC add-binary
        """
        result = []
        m = len(a)
        n = len(b)
        i = m - 1
        j = n - 1
        carry = 0
        while i >= 0 and j >= 0:
            if a[i] == '1' and b[j] == '1':
                next_carry = 1
                result.append(carry)
            elif a[i] == '0' and b[j] == '0':
                next_carry = 0
                result.append(carry)
            else:
                if carry == 1:
                    next_carry = 1
                    result.append(0)
                else:
                    next_carry = 0
                    result.append(1)
            carry = next_carry
            i -= 1
            j -= 1
        
        while i >= 0:
            next_carry = (carry + int(a[i])) // 2
            result.append((carry + int(a[i])) % 2)
            carry = next_carry
            i -= 1
            
        while j >= 0:
            next_carry = (carry + int(b[j])) // 2
            result.append((carry + int(b[j])) % 2)
            carry = next_carry
            j -= 1
        if carry > 0:
            result.append(1)
        
        return "".join(map(lambda x: str(x), result[::-1]))