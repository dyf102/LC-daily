class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """LC 215. Kth Largest Element in an Array
        Quick select 
        Time complexity: O(k*Log(N)) we assume pivot will can divide the list into half everytime
        """
        n = len(nums)

        low = 0
        high = n - 1
        while low < high:
            left = low
            right = high
            pivot = nums[right]
            while left < right:
                while left < right and nums[left] > pivot:
                    left += 1
                while right > left and nums[right] <= pivot:
                    right -= 1
                nums[left], nums[right] = nums[right], nums[left]
            nums[left], nums[high] = nums[high], nums[left]
            if left == k - 1:
                return nums[left]
            elif left < k - 1:
                low = right + 1
            else:
                high = right - 1
        return nums[low]