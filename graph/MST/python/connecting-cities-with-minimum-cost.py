from typing import List
import heapq

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        """1135. Connecting Cities With Minimum Cost
        Time complexity: O(N*Log(E))
        Medium
        There are N cities numbered from 1 to N.
        You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  
        (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)
        Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.
        Example 1:
            Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
            Output: 6
            Explanation: 
            Choosing any 2 edges will connect all cities so we choose the minimum 2.
        Example 2:
            Input: N = 4, connections = [[1,2,3],[3,4,4]]
            Output: -1
            Explanation: 
            There is no way to connect all cities even if all edges are used.
        Note:
        1 <= N <= 10000
        1 <= connections.length <= 10000
        1 <= connections[i][0], connections[i][1] <= N
        0 <= connections[i][2] <= 10^5
        connections[i][0] != connections[i][1]
        """
        pq = [(0, 0)]
        visited = [False] * N
        _map = [[10**6] * N for _ in range(N)]
        for conn in connections:
            c1, c2, w = conn[0] - 1, conn[1] - 1, conn[2]
            _map[c1][c2] = min(_map[c1][c2], w)
            _map[c2][c1] = min(_map[c2][c1], w)
        i = 0
        mst = 0 
        while i < N:
            if len(pq) == 0:
                return -1
            w, v = heapq.heappop(pq)
            # print(w, v, _map[v])
            mst += w
            visited[v] = True
            i += 1
            for _next in range(N):
                if _map[v][_next] != 10**6 and not visited[_next]:
                    heapq.heappush(pq, (_map[v][_next], _next))
        return mst
if __name__ == "__main__":
    s = Solution()
    print(s.minimumCost(1, []))
    print(s.minimumCost(3, [[1,2,5],[1,3,6],[2,3,1]]))
    print(s.minimumCost(4, [[1,2,3],[3,4,4]]))
    print(s.minimumCost(4, [[1,2,3],[2,3,4], [2,4,1], [3,4,4]]))


            