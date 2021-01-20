class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """LC 1584. Min Cost to Connect All Points
        Time complexity: O(V^2)
        Space: O(V^2)
        Naive Prime algorithm to deal with dense graph(E = v^2)
        """
        n = len(points)
        dists = [float('inf')] * n
        _map = [[-1] * n for _ in range(n)]
        visited = [False] * n
        
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, n):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                _map[i][j] = dist
                _map[j][i] = dist
        dists[0] = 0
        mst = 0
        for i in range(n):
            closest = -1
            for j in range(n):
                if not visited[j] and (closest == -1 or dists[closest] > dists[j]):
                    closest = j
            visited[closest] = True
            mst += dists[closest]
            for j in range(n):
                if not visited[j] and _map[closest][j] < dists[j]:
                    dists[j] = _map[closest][j]
        return mst