class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        """LC 1674
        To store and maintain a sorted list of delta
        https://www.youtube.com/watch?v=HvMhvPKjCSU&t=962s
        Args:
            nums (List[int]): [description]
            limit (int): [description]

        Returns:
            int: [description]
        """
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        res = n
        
        for i in range(n // 2):
            a, b = min(nums[i], nums[n - i - 1]), max(nums[i], nums[n - i - 1])
            diff[2] += 2 
            diff[a + 1] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[b + limit + 1] += 1
        
        partial_sum = 0
        for i in range(2, limit*2 + 1):
            partial_sum += diff[i]
            res = min(res, partial_sum)
        return res