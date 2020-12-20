class Solution:
    def minimumDistance(self, word: str) -> int:
        """LC 1320 
            dp[i][l][r] stands min cost to type word[i: n] given l/r fingers position
            TC: O(N*26^2)
        Args:
            word (str): [description]

        Returns:
            int: [description]
        """
        
        def distance(c1, c2):
            if c1 == 27 or c2 == 27: 
                return 0
            distance = abs(c1 // 6 - c2 // 6) + abs(c1 % 6 - c2 % 6)
            # print(v1, v2, distance)
            return distance
        
        def dp(i, n, l, r, memo):
            if i == n:
                return 0
            if memo[i][l][r] != -1:
                return memo[i][l][r]
            c = ord(word[i]) - ord('A') 
            cost = min(dp(i + 1, n, c, r, memo) + distance(l, c), # use left finger to type
                      dp(i + 1, n, l, c, memo) + distance(r, c))  # use right finger to type
            memo[i][l][r] = cost
            return cost
        memo = [[[-1] * 28 for _ in range(28)] for _ in range(len(word))]
        return dp(0, len(word), 27, 27, memo)

    
    def minimumDistance(self, word: str) -> int:
        """Reduce the space to O(26N)
        Because we have the insight, which status of previous finger is always word[i - 1]

        Args:
            word (str): [description]

        Returns:
            int: [description]
        """
        def distance(c1, c2):
            if c1 == 27 or c2 == 27: 
                return 0
            distance = abs(c1 // 6 - c2 // 6) + abs(c1 % 6 - c2 % 6)
            # print(v1, v2, distance)
            return distance
        
        def dp(i, n, r, memo):
            if i == n:
                return 0
            if memo[i][r] != -1:
                return memo[i][r]
            c = ord(word[i]) - ord('A') 
            k = 27 if i == 0 else ord(word[i - 1]) - ord('A') 
            cost = min(dp(i + 1, n, r, memo) + distance(k, c), 
                       dp(i + 1, n, k, memo) + distance(r, c))
            memo[i][r] = cost
            return cost
        memo = [[-1] * 28 for _ in range(len(word))]
        return dp(0, len(word), 27, memo)