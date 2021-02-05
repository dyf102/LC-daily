class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """LC 212. Word Search II
        Use trie to narrow down search direction similar to topological sort
        We use K to denote the longest word in the words
        Time complexity: O(M^2*N^2)
        Space: O(M*N)
        """
        trie = {}
        
        for word in words:
            ptr = trie
            for c in word:
                if c not in ptr:
                    ptr[c] = {}
                ptr = ptr[c]
            ptr['#'] = '#'
        m = len(board)
        n = len(board[0])
        check = [[False] * n for _ in range(m)]
        result = []
        def dfs(i, j, ptr, current):
            direction = [0, 1, 0, -1, 0]
            if '#' in ptr:
                del ptr['#']
                result.append("".join(current))
            for k in range(4):
                x = i + direction[k]
                y = j + direction[k + 1]
                if  0 <= x < m and 0 <= y < n and not check[x][y]:
                    _next = board[x][y]
                    if _next in ptr:
                        check[x][y] = True
                        current.append(_next)
                        dfs(x, y, ptr[_next], current)
                        current.pop()
                        check[x][y] = False
                        
        for i in range(m):
            for j in range(n):
                c = board[i][j]
                if c in trie:
                    check[i][j] = True
                    dfs(i, j, trie[c], [c])
                    check[i][j] = False
        return result
                