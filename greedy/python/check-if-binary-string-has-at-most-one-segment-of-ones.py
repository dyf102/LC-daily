class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """LC 1784. Check if Binary String Has at Most One Segment of Ones
        two pointers
        """
        n = len(s)
        if n == 1:
            return True
        num_seg = 0
        left = right = 0
        while right < n:
            if s[right] == '1':
                right += 1
            else:
                if right - left >= 1:
                    num_seg += 1
                while right < n and s[right] == '0':
                    right += 1
                left = right
        if right - left >= 1:
            num_seg += 1
        return num_seg == 1