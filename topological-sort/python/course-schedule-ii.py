class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """LC 210 Course Schedule II
        Time Complexity: O(N + E)
        Space: O(E)
        Difficulty: Medium
        Keep expanding the result list
        """
        indegrees = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            src, des = prereq[0], prereq[1]
            indegrees[src] += 1
            adj_list[des].append(src)
        
        result = [idx for idx, indegree in enumerate(indegrees) if indegree == 0]
        i = 0
        while i < len(result):
            for _next in adj_list[result[i]]:
                indegrees[_next] -= 1
                if indegrees[_next] == 0:
                    result.append(_next)
            i += 1
        return result if len(result) == numCourses else []