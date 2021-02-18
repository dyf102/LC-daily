class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """LC 1760. Minimum Limit of Balls in a Bag
        
        Args:
            nums (List[int]): [description]
            maxOperations (int): [description]

        Returns:
            int: [description]
        """
        left = 1
        right = 10**9
        nums.sort(reverse=True)
        n = len(nums)
        while left < right:
            middle = (left + right) // 2
            count = 0
            for num in nums:
                count += (num - 1) // middle
            
            if count > maxOperations:
                left = middle + 1
            else:
                right = middle
        return right