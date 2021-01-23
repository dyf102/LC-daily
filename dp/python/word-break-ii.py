class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """LC 140. Word Break II
        top-bottom approach
        Time complexity: O(N^2)
        """
        n = len(s)
        dp = [[] for _ in range (n + 1)]
        
        dp[0] = [0]
        result = []
        wordSet = set(wordDict)

        for i in range(1, n + 1):
            for j in range(i):
                if len(dp[j]) > 0 and s[j: i] in wordSet:
                    dp[i].append(j)
        stack = [(idx, [s[idx: n]]) for idx in dp[n]]
        while len(stack) > 0:
            node, current = stack.pop()
            if node == 0:
                result.append(" ".join(current[::-1]))
            else:
                for _next in dp[node]:
                    copy = current[:]
                    copy.append(s[_next: node])
                    stack.append((_next, copy))
        
        return result

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[] for _ in range (n + 1)]

        wordSet = set(wordDict)

        def dfs(i):
            if i == n:
                return [[]]
            if len(dp[i]) > 0:
                return dp[i]
            
            for _next in range(i + 1, n + 1):
                if s[i: _next] in wordSet:
                    for candidate in dfs(_next):
                        current = candidate[:]
                        current.append(s[i: _next])
                        dp[i].append(current)
            return dp[i]
        dfs(0)
        return [" ".join(x[::-1]) for x in dp[0]]
                        
                