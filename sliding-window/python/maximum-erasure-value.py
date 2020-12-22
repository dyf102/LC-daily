from collections import Counter

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """LC 1695
        Time complexity: O(N)
        Space: O(N)
        Args:
            nums (List[int]): [description]

        Returns:
            int: [description]
        """
        count = Counter()
        n = len(nums)
        i = j = 0
        _sum = result = 0
        while j < n:
            count[nums[j]] += 1
            _sum += nums[j]
            # maintain uniqueness of the window
            while count[nums[j]] > 1:
                _sum -= nums[i]
                count[nums[i]] -= 1
                i += 1
            j += 1
            result = max(result, _sum)
        return result