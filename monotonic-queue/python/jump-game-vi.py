from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """LC 1696
        Category: DP & monotonic queue
        Time complexity: O(N)
        Space: O(k)
        Args:
            nums (List[int]): [description]
            k (int): [description]

        Returns:
            int: [description]
        """
        window = deque()
        window.append((0, nums[0]))
        n = len(nums)
        
        for i in range(1, n):
            idx, max_val = window[0]
            # delete out-range values from the window
            while len(window) > 0 and i - idx > k:
                window.popleft()
                if len(window) > 0:
                    idx, max_val = window[0]
            val = window[0][1] + nums[i] # get the maximum value
            idx, max_val = window[-1]
            # maintain the non-increasing monotonic queue
            while len(window) > 0 and val > max_val:
                window.pop()
                if len(window) > 0:
                    idx, max_val = window[-1]
            window.append((i, val))
        return window[-1][1]