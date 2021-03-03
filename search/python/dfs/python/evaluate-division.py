from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(graph, src, des, visited):
            if des == src:
                return 1
            for _next, weight in graph[src]:
                if _next in visited:
                    continue
                visited.add(_next)
                result = dfs(graph, _next, des, visited)
                if result != -1:
                    return weight * result
                visited.remove(_next)
            return -1
        
        graph = defaultdict(list)

        result = []
        for idx, equation in enumerate(equations):
            graph[equation[0]].append((equation[1], values[idx]))
            graph[equation[1]].append((equation[0], 1.0/values[idx]))


        for query in queries:
            src, des = query[0], query[1]
            if src not in graph or des not in graph:
                result.append(-1)
            else:
                check = set()
                check.add(src)
                val = dfs(graph, src, des, check)
                result.append(val)
        return result