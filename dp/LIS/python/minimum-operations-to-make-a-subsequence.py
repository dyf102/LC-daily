import bisect

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        """LC 1713. Minimum Operations to Make a Subsequence
        Runtime: O(NLogN)
        Space: O(N)
        Because target is unique so we can convert them to index base,
        the LCS problem becomes a LIS problem.
        The original problem can be solved in O(N^2) time complexity
        LIS can be solve by patiance sort in O(NLog(N)) 
        """
        target_map = dict((v, k) for k, v in enumerate(target))
        
        target_idx = list(range(len(target)))
        # filter not-in-target num
        arr_idx = [target_map[v] for v in arr if v in target_map] 
        lis = []
        for i in arr_idx:
            idx = bisect.bisect_left(lis, i)
            if idx == len(lis):
                lis.append(i)
            else:
                lis[idx] = i
        return len(target) - len(lis)