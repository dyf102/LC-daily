from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: list, k: int) -> int:
        """LC 1425
        Runtime: TLE
        Naive DP solution will lead timeout
        Time Complexity: O(N^2)
        Space: O(N)
        Args:
            nums (List[int]): [description]
            k (int): [description]

        Returns:
            int: [description]
        """
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            # print(i, i-k, dp)
            dp[i] = nums[i]
            for j in range(max(0, i-k), i):
                print(j,i, dp)
                dp[i] = max(dp[i], dp[j] + nums[i])
        return max(dp)
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
        DP with sliding window
        Time Complexity: O(N)
        Space: O(N)
        Args:
            nums (List[int]): [description]
            k (int): [description]

        Returns:
            int: [description]
        """
        n = len(nums)
        if n < 1: return 0
        dp = [0] * n
        queue = deque()

        for i, num in enumerate(nums):
            dp[i] = num
            # trick is to put the dp compute first then maintaining the queue
            if i > 0:
                max_idx = queue[0]
                dp[i] = max(dp[i], nums[i] + dp[max_idx])
            # maintain the monotonic queue
            while len(queue) > 0 and i - queue[0] >= k:
                queue.popleft()
            while len(queue) > 0 and dp[i] > dp[queue[-1]]:
                queue.pop()
            queue.append(i)
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    print(s.constrainedSubsetSum([4681,6466,9411,-5130,6047], 3))