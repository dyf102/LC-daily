import heapq

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """LC 269. Alien Dictionary
        Tricky part is to handle corner and invalid cases
        Idea: build graph from sorted words and conduct BFS with topological sort
        Time complexity: O(Total-len * Log(26))
        """
        indegree = dict()
        graph = dict()
        n = len(words)
        if n == 1:
            return words[0]
        for word in words:
            for c in word:
                graph[c] = []
                indegree[c] = 0
        for i in range(n - 1):
            j = 0
            first, second = words[i], words[i + 1]
            if len(second) < len(first) and first.startswith(second):
                return "" 
            min_len = min(len(first), len(second))
            while j < min_len:
                if first[j] != second[j]:
                    graph[first[j]].add(second[j])
                    break
                j += 1
        for nodes in graph.values():
            for node in nodes:
                indegree[node] += 1 
        # topological sort
        queue = [k for k , v in indegree.items() if v == 0]
        result = []
        while len(queue) > 0:
            current = heapq.heappop(queue)
            result.append(current)
            for _next in graph[current]:
                indegree[_next] -= 1
                if indegree[_next] == 0:
                    heapq.heappush(queue, _next)
        # can't find all charactors for the case like cycle
        if len(result) != len(graph):
            return ""
        return "".join(result)