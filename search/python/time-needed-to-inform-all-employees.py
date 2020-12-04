from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        LC 1376
        top-bottom dfs solution
        space: O(N)
        time: O(N)
        Args:
            n (int): [description]
            headID (int): [description]
            manager (List[int]): [description]
            informTime (List[int]): [description]

        Returns:
            int: [description]
        """
        graph = defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append((i, 0 if i == headID else informTime[manager[i]]))
            
        def dfs(graph, idx, time):
            if idx not in graph:
                return time
            max_time = 0
            for _next, weight in graph[idx]:
                max_time = max(max_time, dfs(graph, _next, time + weight))
            return max_time
        return dfs(graph, headID, 0)
    
    def numOfMinutes2(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """Bottom-up solution
        """
        def dfs(i):
            if manager[i] != -1:
                informTime[i] += dfs(manager[i]) # get its managers cost
                manager[i] = -1 # avoid visiting  twice 
            return informTime[i]
        # for each tree path
        return max(map(dfs, range(n)))