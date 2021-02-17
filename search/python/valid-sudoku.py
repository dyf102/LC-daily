class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square = [[0] * 3 for _ in range(3)]
        horitental = [0] * 9
        vertical = [0] * 9
        
        for x, row in enumerate(board):
            for y, c in enumerate(row):
                if c == '.':
                    continue
                else:
                    v = int(c)
                    if square[x // 3][y // 3] & (1 << v) > 0 or horitental[y] & (1 << v) > 0 \
                    or vertical[x] & (1 << v) > 0:
                        return False
                    square[x // 3][y // 3] |= (1 << v)
                    horitental[y] |= (1 << v)
                    vertical[x] |= (1 << v)
        return True