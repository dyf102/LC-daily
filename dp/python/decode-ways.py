class Solution:
    def numDecodings(self, s: str) -> int:
        """LC 91. Decode Ways

        Args:
            s (str): [description]

        Returns:
            int: [description]
        """
        n = len(s)
        if n == 1: return 0 if s == "0" else 1
        
        dp = [0] * n
        dp[-1] = 0 if s[-1] == "0" else 1
        if s[0] == "0": return 0
        for i in range(n - 1)[::-1]:
            if s[i]  == "1" or (s[i] == "2" and ord(s[i + 1]) <= ord("6")):
                dp[i] = dp[i + 1] + (1 if i > n - 3 else dp[i + 2])
            elif s[i] != "0":
                dp[i] = dp[i + 1]
        # print(dp)
        return dp[0]
                                