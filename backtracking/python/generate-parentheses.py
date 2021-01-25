class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """LC 22. Generate Parentheses
        Time Complexity: O(2^N)
        Use two parameter to control number of ( and ) in order to generate a valid result
        """
        result = []
        def backtracing(start, end, current):
            if start == n and end == n:
                # print(current)
                result.append("".join(current))
            elif start == n:
                current.append(")")
                backtracing(start, end + 1, current)
                current.pop()
            else:
                if start == end:
                    current.append("(")
                    backtracing(start + 1, end, current)
                    current.pop()
                elif start > end:
                    current.append("(")
                    backtracing(start + 1, end, current)
                    current.pop()
                    current.append(")")
                    backtracing(start, end + 1, current)
                    current.pop()
        backtracing(0, 0, [])
        return result