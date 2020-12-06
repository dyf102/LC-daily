from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        """ LC 1031
        Time complexity: O(N^2)
        Space complexity: O(N)
        Args:
            A (List[int]): [description]
            L (int): [description]
            M (int): [description]

        Returns:
            int: [description]
        """
        partial_sum = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            partial_sum[i] = partial_sum[i - 1] + A[i - 1]
        result = 0
        for i in range(L - 1,len(A)):
            sum1 = partial_sum[i + 1] - partial_sum[i + 1 - L]
            for j in range(M - 1, len(A)):
                if j <= i - L or j - M >= i:
                    sum2 = partial_sum[j + 1] - partial_sum[j + 1 - M]
                    result = max(result, sum1 + sum2)
        return result