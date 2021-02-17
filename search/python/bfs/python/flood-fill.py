from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """LC 733 Floor fill 
        Time complexity: O(E + N)
        Space O(N)
        Difficulty: easy
        Args:
            image (List[List[int]]): [description]
            sr (int): [description]
            sc (int): [description]
            newColor (int): [description]

        Returns:
            List[List[int]]: [description]
        """
        queue = deque()
        m = len(image)
        n = len(image[0])
        check = [[False] * n for _ in range(m)]
        queue.append((sr, sc))
        check[sr][sc] = True
        target = image[sr][sc]
        while len(queue) > 0:
            x, y = queue.popleft()
            image[x][y] = newColor
            direction = [0, 1, 0, -1, 0]
            for i in range(4):
                next_x, next_y = x+direction[i], y + direction[i + 1]
                if 0 <= next_x < m and 0 <= next_y < n and not check[next_x][next_y] and image[next_x][next_y] == target:
                    queue.append((next_x, next_y))
                    check[next_x][next_y] = True
        return image