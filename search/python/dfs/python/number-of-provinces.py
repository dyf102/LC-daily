class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """LC 547 Number of Provinces
        N: num of edge
        M: num of node
        Complexity: O(N + M)
        It can also be solved via union find
        Args:
            isConnected (List[List[int]]): [description]

        Returns:
            int: [description]
        """
        n = len(isConnected)
        if n == 0:
            return 0
        check = [False] * n
        res = 0
        def dfs(x):
            check[x] = True
            for i in range(n):
                if i != x and not check[i] and isConnected[x][i] == 1:
                    dfs(i)
        for i in range(n):
            if  not check[i]:
                res += 1
                dfs(i)
        return res