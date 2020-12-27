from collections import defaultdict, deque
from typing import List

def shortestPathLength(graph: List[List[int]]) -> int:
    """LC 847
    Time complexity: O(N*2^N)
    Space: O(N*2^N)
    A pure BFS solution. It uses bit covery to store the status.
    Args:
        graph (List[List[int]]): [description]

    Returns:
        int: [description]
    """
    n = len(graph)
    target = (2 ** n) - 1
    queue = deque([(1 << i, i) for i in range(n)])
    seen = [[0] * (2 ** n) for _ in range(n)]
    step = 0
    while len(queue) > 0:
        current = len(queue)
        for i in range(current):
            s, ending = queue.popleft()
            if seen[ending][s] == 1:
                continue
            # Since it's bfs, we can assure the first is shortest
            if s == target: return step
            seen[ending][s] = 1
            for nxt in graph[ending]:
                next_s = s |(1 << nxt)
                queue.append((next_s, nxt))
        step += 1

if __name__ == "__main__":
    print(shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))