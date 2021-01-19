
class Solution:
    def minCostToSupplyWater(self, n: int, wells, pipes) -> int:
        root = list(range(n + 1))
        def findRoot(idx):
            if root[idx] != idx:
                root[idx] = findRoot(root[idx])
            return root[idx]
        
        def union(first, second):
            p1 = findRoot(first)
            p2 = findRoot(second)
            if p1 != p2:
                root[p2] = p1
        
        _map = [[0] * (n + 1) for _ in range(n + 1)]
        for idx, well in enumerate(wells):
            _map[0][idx + 1] = well

        for pipe in pipes:
            _map[pipe[0]][pipe[1]] = pipe[2]
            _map[pipe[1]][pipe[0]] = pipe[2]
        
        pipes.sort(key=lambda x: x[2])

        mst = 0
        i = 0
        for pipe in pipes:
            s, d, w = pipe[0], pipe[1], pipe[2]
            if findRoot(s) != findRoot(d):
                union(s, d)
                mst += w
                i += 1
                if i == n: # early stop
                    break
        return mst

if __name__ == "__main__":
    s = Solution()
    print(s.minCostToSupplyWater(3, [1,2,2], [[1,2,1],[2,3,1]]))