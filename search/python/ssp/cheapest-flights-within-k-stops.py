from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        """LC 787. Cheapest Flights Within K Stops
        Modified Dikistra SSP search
        The constrain is the graph is acyclic and has positive weights(No negative cycle)
        we can't use the regular relaxation 
        Time complexity: O(E + )
        """
        adj_list = defaultdict(list)
        for edge in flights:
            adj_list[edge[0]].append((edge[1], edge[2]))
        heap = [(0, K, src)]
        while heap:
            w, stop, node = heappop(heap)
            if node == dst:
                return w
            if stop >= 0:
                for _next, n in adj_list.get(node, []):
                    # if dist[node] + w < dist[_next]:
                    heappush(heap, (w + n, stop - 1, _next))
        return -1
                