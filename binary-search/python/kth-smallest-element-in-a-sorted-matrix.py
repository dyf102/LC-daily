import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """LC 378. Kth Smallest Element in a Sorted Matrix
        Time complexity: O(N*N * Log(k))
        """
        m = len(matrix)
        n = len(matrix[0])
        
        heap = []
        
        for i in range(m):
            for j in range(n):
                v = matrix[i][j]
                if len(heap) < k:
                    heapq.heappush(heap, -v)
                elif v < -heap[0]:
                    heapq.heappushpop(heap, -v)
        return -heap[0]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Binary search approach
        Time complexity: O(N * Log(31))
        """
        m = len(matrix)
        n = len(matrix[0])
        
        left = matrix[0][0]
        right = matrix[-1][-1]
        def equalOrSmaller(target):
            x = m - 1
            y = 0
            count = 0
            while x >= 0 and y < n:
                if matrix[x][y] <= target:
                    count += (x + 1)
                    y += 1
                else:
                    x -= 1
            return count
        
        while left < right:
            middle = (left + right) // 2
            c = equalOrSmaller(middle)
            if c < k: # too small
                left = middle + 1 # value will be in left 
            else:
                right = middle
        return left