class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """LC 646. Maximum Length of Pair Chain
        Time complexity: O(N^2)
        Space: O(N)
        """
        starts, ends = zip(*sorted(pairs))
        n = len(pairs)
        dp = [1] * n
        result = 1
        # print(starts, ends)
        for i in range(n):
            for j in range(i):
                if ends[j] < starts[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)