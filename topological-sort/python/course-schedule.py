from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Topological sort
        Time Complexity: O(N + E)
        Space: O(N)
        """
        indegree = [0] * numCourses
        _map = [[] for _ in range(numCourses)]
        for prerequisit in prerequisites:
            src, des = prerequisit[0], prerequisit[1]
            if indegree[des] == 0:
                indegree[des] += 1
            _map[src].append(des)
        queue = deque([i for i, x in enumerate(indegree) if x == 0])
        
        count = 0
        while len(queue) > 0:
            i = queue.popleft()
            count += 1
            for _next in range(numCourses):
                if _map[i][_next] == 1:
                    if indegree[_next] == 1:
                        queue.append(_next)
                    indegree[_next] -= 1
        return count == numCourses
    
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """DFS method
        
        """
        _map = [[] for _ in range(numCourses)]
        for prerequisit in prerequisites:
            src, des = prerequisit[0], prerequisit[1]
            _map[des].append(src)
        check = [False] * numCourses
        def dfs(i):
            if check[i]:
                return False
            check[i] = True
            for _next in _map[i]:
                if not dfs(_next):
                    return False
            check[i] = False
            return True
        for start in range(numCourses): 
            if not dfs(start):
                return False
        return True