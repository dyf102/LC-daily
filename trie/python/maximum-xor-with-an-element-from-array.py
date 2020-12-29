import bisect

class Trie:
    def __init__(self):
        self.children = [None] * 2
    def add(self, num):
        ptr = self
        for i in range(31)[::-1]:
            bit = num >> i & 1
            if ptr.children[bit] is None:
                _next = Trie()
                ptr.children[bit] = _next
            ptr = ptr.children[bit]
    def get_max(self, num):
        maximum = num
        ptr = self
        for i in range(31)[::-1]:
            bit = (num >> i) & 1
            opposite = bit ^ 1
            if ptr.children[opposite]:
                maximum ^= (opposite << i)
                ptr = ptr.children[opposite]
            elif ptr.children[bit]:
                maximum ^= (bit << i)
                ptr = ptr.children[bit]
        return maximum
            
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """LC 1707 Maximum XOR With an Element From Array
        M queries
        N nums
        Constant time to add and get_max from a trie
        Time Complexity: O(M*Log(M) + N*Log(N) + Log(N)*M)
        Space: O(2^32) constant space
        Args:
            nums (List[int]): [description]
            queries (List[List[int]]): [description]

        Returns:
            List[int]: [description]
        """
        queries = sorted([(x[1], x[0], i) for i, x in enumerate(queries)])
        queries.sort()
        nums.sort()
        last_idx = 0
        root = Trie()
        result = [0] * len(queries)
        for m, x, idx in queries:
            curr_idx = bisect.bisect_right(nums, m)
            if curr_idx == 0:
                result[idx] = -1
                continue
            for i in range(last_idx, curr_idx):
                root.add(nums[i])
            result[idx] = root.get_max(x)
            last_idx = curr_idx
        return result