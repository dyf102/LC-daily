import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """LC 300. Longest Increasing Subsequence

        Args:
            nums (List[int]): [description]

        Returns:
            int: [description]
        """
        lls = []
        for num in nums:
            idx = bisect.bisect_left(lls, num)
            if idx == len(lls):
                lls.append(num)
            else:
                lls[idx] = num
        return len(lls)