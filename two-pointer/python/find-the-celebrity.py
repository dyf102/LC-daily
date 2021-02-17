class Solution:
    def findCelebrity(self, n: int) -> int:
        """LC 277. Find the Celebrity
        """
        left = 0
        right = n - 1
        while left < right:
            if knows(left, right):
                left += 1
            else:
                right -= 1
        for i in range(n):
            if i != left:
                if not knows(i, left):
                    return -1
                if knows(left, i):
                    return -1
        return left