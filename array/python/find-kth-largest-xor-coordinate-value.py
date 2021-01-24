from typing import List
import heapq
import copy

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        """LC 1738. Find Kth Largest XOR Coordinate Value
        matrix[i][j] = matrix[i - 1][j] ^ matrix[i][j - 1] ^ matrix[i - 1][j - 1]
        Similar to trangle sum in matrix
        Time complexity: O(M * N)
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] ^= matrix[i][j - 1]
        for j in range(n):
            for i in range(1, m):
                matrix[i][j] ^= matrix[i - 1][j]
        
        heap = []
        
        for i in range(m):
            for j in range(n):
                if len(heap) < k:
                    heapq.heappush(heap, matrix[i][j])
                elif matrix[i][j] > heap[0]:
                    heapq.heappushpop(heap, matrix[i][j])
        return heap[0]
    
    def kthLargestValue2(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        result = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] ^ dp[i][j - 1] ^ dp[i - 1][j - 1] ^ matrix[i - 1][j - 1]   
                result.append(dp[i][j])
        return sorted(result, reverse=True)[:k][-1]