class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """LC 16. 3Sum Closest
        Time complexity: O(N^2)
        
        """
        nums.sort()
        i = 0
        n = len(nums)
        result = float('inf')
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum < target:
                    j += 1
                else:
                    k -= 1
                if abs(_sum - target) < abs(result - target):
                    result = _sum
        return result
        