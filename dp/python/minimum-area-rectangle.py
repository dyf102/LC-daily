from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """Time complexity: O(N^2)
        space: O(N)
        runtime: 1864 ms 
        Args:
            words (List[str]): [description]

        Returns:
            int: [description]
        """
        
        words.sort(key=len)
        def is_predecessor(s1, s2):
            if len(s1) + 1 != len(s2):
                return False
            i = j = 0
            diff = 0
            while i < len(s1) and j < len(s2):
                if s1[i] != s2[j]:
                    diff += 1
                    j += 1
                    if diff > 1:
                        return False
                else:
                    i += 1
                    j += 1
            return True
        n = len(words)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i)[::-1]:
                if len(words[i]) - len(words[j]) > 1:
                    break
                if is_predecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    def  longestStrChain2(self, words: List[str]) -> int:
        """
        Faster implementation

        Args:
            words (List[str]): [description]

        Returns:
            int: [description]
        """

        words.sort(key=len)
        dp = {}
        for w in words:
            dp[w] = max([dp.get(w[:i] + w[i+1:], 0) + 1 for i in range(len(w))])
        return max(dp.values())