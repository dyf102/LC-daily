class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """LC 416 Partition Equal Subset Sum
        Tim complexity: O(N * max(nums))
        difficulty: medium
        Args:
            nums (List[int]): [description]

        Returns:
            bool: [description]
        """
        n = len(nums)
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        target = _sum // 2
        dp = [[False] * (target + 1) for _ in range(n)]

        for i in range(0, n):
            if nums[i] > target: continue
            dp[i][nums[i]] = True
            if i == 0: continue
            for j in range(target + 1):
                if j >= nums[i] and dp[i - 1][j - nums[i]]:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i - 1][j]
            if dp[i][target]:
                return True
        return False

    def canPartition(self, nums: List[int]) -> bool:
        """Space optimization version
        """
        n = len(nums)
        _sum = sum(nums)
        if _sum % 2 != 0:
            return False
        target = _sum // 2
        dp = [False] * (target + 1)

        for i in range(0, n):
            if nums[i] > target: continue
            dp[nums[i]] = True
            if i == 0: continue
            for j in range(target + 1):
                if j >= nums[i] and dp[j - nums[i]]:
                    dp[j] = True
            if dp[target]:
                return True
        return False