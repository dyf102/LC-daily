import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        """LC 1705 Maximum Number of Eaten Apples
        time complexity: O(N*Log(N))
        space: O(N)
        Args:
            apples (List[int]): [description]
            days (List[int]): [description]

        Returns:
            int: [description]
        """
        heap = []
        n = len(apples)
        
        result = 0
        i = 0
        while i < n or len(heap) > 0:
            if i < n and apples[i] != 0:
                heapq.heappush(heap, [i + days[i], apples[i]])
            while len(heap) > 0 and (heap[0][1] <= 0 or heap[0][0] <= i):
                heapq.heappop(heap)
            if heap:
                result += 1
                heap[0][1] -= 1
            i += 1
        return result