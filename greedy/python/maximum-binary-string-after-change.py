class Solution:
    def maximumBinaryString(self, s):
        """LC 1702 Maximum Binary String After Change
        Difficulty: Medium
        Time complexity: O(N)
        space: O(1)
        Args:
            s ([type]): [description]

        Returns:
            [type]: [description]
        """
        if s.find('0') == -1: return s
        k, n = s.count('1', (s + '0').find('0')), len(s)
        return '1' * (n - k - 1) + '0' + '1' * k