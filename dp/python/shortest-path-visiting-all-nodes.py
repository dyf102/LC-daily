from collections import deque

def shortestPathLength(self, graph: List[List[int]]) -> int:
    """LC 847

    Args:
        graph (List[List[int]]): [description]

    Returns:
        int: [description]
    """
    n = len(graph)
    target = (2 ** n) - 1
    queue = deque([(1 << i, i) for i in range(n)])
    dp = [[float('inf')] * n for _ in range(2 ** n)]
    step = 0
    seen = {}
    while len(queue) > 0:
        current = len(queue)
        for i in range(current):
            s, ending = queue.popleft()
            dp[s][ending] = min(dp[s][ending], step)
            for nxt in graph[ending]:
                next_s = s |(1 << nxt)
                if (next_s, nxt) in seen:
                    continue
                seen[(next_s, nxt)] = 1
                queue.append((next_s, nxt))
        step += 1
    return min(dp[-1])