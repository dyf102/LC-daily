class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """LC 821. Shortest Distance to a Character
        Time complexity: O(N)
        """
        pos = []
        
        prev = -1000
        j = 0
        for i, c2 in enumerate(s):
            if c2 == c:
                while j < i:
                    pos.append(min(j - prev, i - j))
                    j += 1
                prev = i
                j = i
        while j < len(s):
            pos.append(j - prev)
            j += 1
        return pos
                