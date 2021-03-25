import math as m

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        """LC 1785. Minimum Elements to Add to Form a Given Sum

        """
        total = sum(nums)
        
        diff = goal - total
        return m.ceil(abs(diff) / limit)