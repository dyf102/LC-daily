class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """using monotonically increasing stack
        LC 1673
        Args:
            nums (List[int]): [description]
            k (int): [description]

        Returns:
            List[int]: result
        """
        if len(nums) == 0:
            return []
        stack = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            left = n - i
            # check whether there is enouth number to build size k array
            while len(stack) > 0 and left + len(stack) > k and nums[i] < stack[-1]:
                stack.pop()
            if len(stack) < k:
                stack.append(nums[i])
        return stack
 