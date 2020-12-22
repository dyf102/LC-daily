class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """LC 1697
        Runtime: O(E*Log(E) + N*Log(N))
        E: # of edges
        N: # of queries
        category: union-find
        Args:
            n (int): [description]
            edgeList (List[List[int]]): [description]
            queries (List[List[int]]): [description]

        Returns:
            List[bool]: [description]
        """
        edges = sorted([(e[2], e[0], e[1]) for e in edgeList])
        ordered_queries = sorted([(e[2], e[0], e[1], idx) for idx, e in enumerate(queries)])
        
        root = list(range(n))
        rank = [0] * n
        def find(a):
            if root[a] != a:
                root[a] = find(root[a])
            return root[a]
        
        def union(a, b):
            p1 = find(a)
            p2 = find(b)
            if p1 != p2:
                r1 = rank[p1]
                r2 = rank[p2]
                if r1 < r2:
                    root[p1] = p2
                elif r1 > r2:
                    root[p2] = p1
                else:
                    root[p1] = p2
                    rank[p2] = rank[p1] + 1
        i = 0
        res = [False] * len(queries)
        for w, s, e, idx in ordered_queries:
            if i < len(edges):
                w2, s2, e2 = edges[i]
                while w2 < w:
                    union(s2, e2)
                    i += 1
                    if i >= len(edgeList): 
                        break
                    w2, s2, e2 = edges[i]
            p1 = find(s)
            p2 = find(e)
            res[idx] = p1 == p2
        return res
            
                