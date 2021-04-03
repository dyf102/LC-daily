class Solution:
    def simplifyPath(self, path: str) -> str:
        """LC 71. Simplify Path

        Args:
            path (str): [description]

        Returns:
            str: [description]
        """
        n = len(path)
        if n == 0:
            return path
        stack = []
        
        i = 1
        while i < n:
            current = []
            while i < n and path[i] != '/':
                current.append(path[i])
                i += 1
            current = "".join(current)
            if current == '.' or current == '':
                i += 1
                continue
            elif current == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(current)
            i += 1
        return '/' + '/'.join(stack)

if __name__ == "__main__":
    s = Solution()
    s.simplifyPath("/hello../world")