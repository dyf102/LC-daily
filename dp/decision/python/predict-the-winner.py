

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """LC 486. Predict the Winner
        top-bottom approach
        """
        @lru_cache()
        def dp(i, j):
            if i == j:
                return nums[i]
            elif i > j:
                return 0
            return max([min([dp(i + 2, j), dp(i + 1, j - 1)]) + nums[i], 
            min([dp(i + 1, j - 1), dp(i, j - 2)]) + nums[j]])
        
        total = sum(nums)
        v = dp(0, len(nums) - 1)
        return  v >= total - v # tier case
    
    def PredictTheWinner2(self, nums: List[int]) -> bool:
        """Space optimization version
        """
        @lru_cache()
        def dp(i, j):
            if i == j:
                return nums[i]
            return max([nums[i] - dp(i + 1, j), nums[j] - dp(i, j - 1)])
        return dp(0, len(nums) - 1) >= 0