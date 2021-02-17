class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        square = [[0] * 3 for _ in range(3)]
        horitental = [0] * 9
        vertical = [0] * 9
        check = [[0] * 9 for _ in range(9)]
        count = 0
        for x, row in enumerate(board):
            for y, c in enumerate(row):
                if c == '.':
                    count += 1
                else:
                    v = int(c)
                    square[x // 3][y // 3] |= (1 << v)
                    horitental[x] |= (1 << v)
                    vertical[y] |= (1 << v)
       
        def backtracking(i, j, current):
            # print(i , j, bin(square[i // 3][j // 3]),  bin(horitental[i]),  bin(vertical[j]))
            direction = [0, 1, 0, -1, 0]
            if board[i][j] == '.':
                for v in range(1, 10):
                    join_set = square[i // 3][j // 3] | horitental[i] | vertical[j]
                    # print(bin(join_set))
                    if join_set == (1 << 10) - 2:
                        return False
                    if join_set & (1 << v) == 0:
                        board[i][j] = str(v)
                        if current + 1 == count:
                            return True
                        square[i // 3][j // 3] |= (1 << v)
                        horitental[i] |= (1 << v)
                        vertical[j] |= (1 << v)
                        for n in range(4):
                            next_x = i + direction[n]
                            next_y = j + direction[n + 1]
                            if  0 <= next_x < 9 and 0 <= next_y < 9 and check[next_x][next_y] == 0:
                                check[next_x][next_y] = 1
                                if backtracking(next_x, next_y, current + 1):
                                    return True
                                else:
                                    check[next_x][next_y] = 0
                                    break
                                check[next_x][next_y] = 0
                        board[i][j] = '.'
                        square[i // 3][j // 3] ^= (1 << v)
                        horitental[i] ^= (1 << v)
                        vertical[j] ^= (1 << v)
            else:
                for n in range(4):
                    next_x = i + direction[n]
                    next_y = j + direction[n + 1]
                    if  0 <= next_x < 9 and 0 <= next_y < 9 and check[next_x][next_y] == 0:
                        check[next_x][next_y] = 1
                        if backtracking(next_x, next_y, current):
                            return True
                        check[next_x][next_y] = 0
            return False
        check[0][0] = 1
        
        backtracking(0, 0, 0)
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s = Solution()
s.solveSudoku(board)
print(board)