class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """LC 28. Implement strStr()
        Naive implementation
        Time complexity: O(M*N)
        """
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        elif n > m:
            return -1
        i =  0
        while i <  (m - n + 1):
            k = 0
            while k < n and haystack[i + k] == needle[k]:
                k += 1
            if k == len(needle):
                return i
            i += 1
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        """KMP implementation
        """
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        elif n > m:
            return -1
        nexts = [0] * n
        for i in range(2, n):
            if needle[i - 1] == needle[nexts[i - 1]]:
                nexts[i] = nexts[i - 1] + 1
        # print(dp)
        i = k = 0
        while i <  (m - n + 1):
            while k < n and haystack[i + k] == needle[k]:
                k += 1
            if k == len(needle):
                return i
            else:
                k = nexts[k]
            i += 1
        return -1