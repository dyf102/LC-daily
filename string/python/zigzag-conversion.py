class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """LC 6 ZigZag Conversion
        Time complexity: O(N)
        Space: O(N)
        """
        if numRows == 1:
            return s
        result = [[] for _ in range(numRows)]
        
        curr_row = 0
        diff = 1
        for i in range(len(s)):
            result[curr_row].append(s[i])
            curr_row += diff
            if curr_row == 0:
                diff = 1
            elif curr_row == numRows - 1:
                diff = -1
        result_c = []
        for row in result:
            for c in row:
                result_c.append(c)
        return "".join(result_c)