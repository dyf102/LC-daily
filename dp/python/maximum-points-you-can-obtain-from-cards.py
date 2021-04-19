class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """LC 1423. Maximum Points You Can Obtain from Cards
        O(N^2) timeout
        """
        n = len(cardPoints) - 1
        
        @lru_cache()
        def dfs(start, i):
            if i == k:
                return 0
            return max(cardPoints[n - start - i] + dfs(start, i + 1), cardPoints[start] + dfs(start + 1, i + 1))
        
        return dfs(0, 0)

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """ O(N) moving window
        """
        dp = [0] * (k + 1)
        n = len(cardPoints)
        dp[0] = sum(cardPoints[n - k:])
        result = dp[0]
        for i in range(1, k + 1):
            dp[i] = cardPoints[i - 1] + dp[i - 1] - cardPoints[n - k + i - 1]
            result = max(dp[i], result)
        return result

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """ O(N) moving window
        """
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        k = n - k
        head = k     
        current = sum(cardPoints[:k])
        minimum = current
        while head < n:
            current += (cardPoints[head] - cardPoints[head - k])
            minimum = min(minimum, current)
            head += 1
        return sum(cardPoints) - minimum