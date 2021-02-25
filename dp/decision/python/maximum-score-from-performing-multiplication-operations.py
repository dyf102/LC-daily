from functools import lru_cache

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        """LC 1770. Maximum Score from Performing Multiplication Operations
        Top-bottom approach:
        start is left index, end is right index and i is index of multipliers
        because each time we increase i and move start or end there is a relation
        i = start + (n - end), therefore we squeeze the dp space into M*N instead of 
        M * N^2, we can reduce the space furthermore by using bottom-up approach 
        because the status is only depending on previous status, so we don't have
        to store all status along N (size of multipliers)
        """
        n = len(multipliers)
        @lru_cache(2000)
        def solver(start, end, i):
            if i == n:
                return 0
            return max(nums[start] * multipliers[i] + solver(start + 1, end, i + 1 ),\
            nums[end] * multipliers[i] + solver(start, end - 1, i + 1))
        return solver(0, len(nums) - 1, 0)

    def maximumScore2(self, nums: List[int], multipliers: List[int]) -> int:
        """Bottom-up approach
        TODO: Finish it
        """
        pass