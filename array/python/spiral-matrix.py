class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """LC 

        Args:
            matrix (List[List[int]]): [description]

        Returns:
            List[int]: [description]
        """
        m = len(matrix)
        if m == 0:
            return []
        elif m == 1:
            return matrix[0]
        n = len(matrix[0])
        if n == 1:
            return [row[0] for row in matrix]
        count = 0
        visted = [[False] * (n) for _ in range(m)]
        direction = [0, 1, 0, -1, 0]
        direction_idx = 0
        x = y = 0
        result = []
        while True:
            result.append(matrix[x][y])
            visted[x][y] = True
            count += 1
            if count == (m * n): # post condition
                break
            next_x = x + direction[direction_idx]
            next_y = y + direction[direction_idx + 1]
            # boundry case
            while next_x < 0 or next_y < 0 or next_x >= m or next_y >= n or visted[next_x][next_y]:
                direction_idx = (direction_idx + 1) % 4
                next_x = x + direction[direction_idx]
                next_y = y + direction[direction_idx + 1]
            x, y = next_x, next_y
        return result