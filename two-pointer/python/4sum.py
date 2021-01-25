class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """LC 18. 4Sum
        Two sum related question, be careful about the deduplicating nums
        Time complexity: O(N^3)
        """
        result = []
        n = len(nums)
        if n < 4: return []
        nums.sort()
        
        
        def twoSum(start, target):
            left = start
            right = n - 1
            while left < right:
                if left > start and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                if right < n - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue
                _sum = nums[left] + nums[right]
                if _sum == target:
                    yield (nums[left], nums[right])
                    left += 1
                    right -= 1
                elif _sum < target:
                    left += 1
                else:
                    right -= 1
            
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]: 
                    continue
                for v2, v3 in twoSum(j + 1, target - (nums[i] + nums[j])):
                    result.append([nums[i], nums[j], v2, v3])
        return result
        