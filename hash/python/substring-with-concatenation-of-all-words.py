from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """LC 30. Substring with Concatenation of All Words
        
        """
        i = 0
        n = len(s)
        m = len(words[0])
        counter = Counter(words)
        current = Counter()
        count = 0
        result = []
        while i <= n - count * m:
            j = i
            while j <= n and s[j: j + m] in counter:
                tmp = s[j: j + m]
                current[tmp] += 1
                count += 1
                j += m
                if current[tmp] > counter[tmp]:
                    break
                if current == counter:
                    result.append(j - count * m)
                    break
            count = 0
            current = Counter()
            i += 1
        return result