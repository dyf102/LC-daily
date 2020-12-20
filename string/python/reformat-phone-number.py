class Solution:
    def reformatNumber(self, number: str) -> str:
        """LC 1694
        Time complexity: O(N)
        Space complexity: O(N)
        Args:
            number (str): [description]

        Returns:
            str: [description]
        """
        digits = []
        for c in number:
            if c.isdigit():
                digits.append(c)
        result = []
        n = len(digits)
        i = 0
        while n >= 4:
            result.append(digits[i: i + 3])
            i += 3
            n -= 3
        if n == 4:
            result.append(digits[i: i + 2])
            i += 2
            result.append(digits[i: i + 2])
        elif n == 1:
            if len(result) > 0:
                last = result.pop()
                result.append(last[:2])
                tmp = last[2:]
                tmp.append(digits[i])
                result.append(tmp)
        else:
            result.append(digits[i:])
        return "-".join(map(lambda x: "".join(x), result))
                