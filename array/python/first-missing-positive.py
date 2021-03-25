class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """LC 41. First Missing Positive
        Time complexity: O(N)
        Space: O(N)
        """
        if len(nums) == 0:
            return 1
        minimum = max([min(nums), 0])
        maximum = max([max(nums), 0])
        check = {}
        
        for num in nums:
            if num > 0:
                check[num] = True

        for i in range(1, maximum + 2):
            if i not in check:
                return i
    
    def firstMissingPositive2(self, nums: List[int]) -> int:
        """No extra space required
        """
        if len(nums) == 0:
            return 1
        idx = 0
        while idx < len(nums):
            num = nums[idx]
            if num - 1 != idx and 0 < num < len(nums) and nums[num - 1] != nums[idx]:
                nums[num - 1], nums[idx] = nums[idx], nums[num - 1]
            else:
                idx += 1
        for idx, num in enumerate(nums):
            if idx + 1 != num:
                return idx + 1
        return len(nums) + 1