from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        LC 410. Split Array Largest Sum
        TTL backtracing solution
        Time Complexity O(N ^ 2)
        """
        n = len(nums)
        group_sum = [0] * m
        
        def dfs(idx, group):
            # print(idx, group, group_sum)
            if idx == n:
                if group == m - 1:
                    return max(group_sum)
                else:
                    return float('inf')
            elif group >= m:
                return float('inf')
            else:
                largest = float('inf')
                group_sum[group] += nums[idx]
                largest = min(largest, dfs(idx + 1, group))
                group_sum[group] -= nums[idx]
                largest = min(largest, dfs(idx, group + 1))
 
            return largest
        return dfs(0, 0)

    def splitArray2(self, nums: List[int], m: int) -> int:
        """Binary search solution
        Time comeplexity: O(21*Log(N))
        """
        n = len(nums)
        def canSplit(target):
            group_sum = 0
            group_count = 1
            for i in range(n):
                if group_sum + nums[i] <= target:
                    group_sum += nums[i]
                else:
                    group_count += 1
                    if group_count > m or nums[i] > target:
                        return False
                    group_sum = nums[i]
            return True # group_count == m
            
        left, right = max(nums), sum(nums)
        
        while left <= right:
            middle = left + (right - left) // 2
            print(left, right, middle, canSplit(middle))
            if canSplit(middle):
                # 2 cases: 1. we have less group than requred. 2. we have exactly # of group
                # we need lower the upper bound to minimize middle
                right = middle - 1
            else:
                # too small, we have too many group
                left = middle + 1
        # when right = left + 1, middle = left
        # then next step calSplit(middle) = True, right = left - 1, so left is smallest value, 
        # which can split the array
        return left
    
    def splitArray(self, nums: List[int], m: int) -> int:
        
        n = len(nums)
        if n == 0: 
            return 0
        dp = [[float('inf')] * n for _ in range(m)]
        partial_sum = [0] * (n + 1)

        dp[0][0] = nums[0]
        partial_sum[0] = nums[0]
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + nums[i]
            partial_sum[i + 1] = partial_sum[i] + nums[i]
        
        
        for j in range(1, m):
            tmp = dp[j - 1]
            for i in range(j, n):
                val = 10000000000
                for k in range(i):
                    val = min(val, max(tmp[k], partial_sum[i + 1] - partial_sum[k + 1]))
                dp[j][i] = val
        return dp[m - 1][n - 1]