import math

class Trie:
    def __init__(self):
        self.children = [None] * 2
    def __str__(self):
        # For debug
        if self.children[0] and self.children[1]:
            return "[0: {}, 1: {}]".format(str(self.children[0]), str(self.children[1]))
        elif self.children[0]:
            return "[0: {}]".format(str(self.children[0]))
        elif self.children[1]:
            return "[1: {}]".format(str(self.children[1]))
        else:
            return "None"

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """LC 421 Maximum XOR of Two Numbers in an Array
        Method 1
        Time complexity: O(N)
        space: O(N)
        """
        max_num = max(nums)
        num_bit = 0 if max_num == 0 else int(math.log(max_num, 2)) + 1
        result = 0
        max_val = 0
        for i in range(num_bit)[::-1]:
            max_val <<= 1
            cur_val = max_val | 1
            prefixs = {num >> i for num in nums}
            max_val |= any(prefix ^ cur_val in prefixs for prefix in prefixs)
        return max_val

    def findMaximumXOR(self, nums: List[int]) -> int:
        """LC 421 Maximum XOR of Two Numbers in an Array
        Method 2
        Time complexity: O(N)
        space: O(2^31)
        Args:
            nums (List[int]): [description]

        Returns:
            int: [description]
        """
        n = len(nums)
        res = 0
        trie = Trie()
        # adding num to trie
        for num in nums:
            ptr = trie
            for i in range(31)[::-1]:
                bit = ((num >> i) & 1)
                _next = ptr.children[bit]
                if _next is None:
                    _next = Trie()
                    ptr.children[bit] = _next
                ptr = _next
        # finding the maximum for each num
        for num in nums:
            current = num
            ptr = trie
            for i in range(31)[::-1]: # constant time complexity
                bit = (num >> i) & 1
                oppo_bit =  bit ^ 1
                if ptr.children[oppo_bit] != None:
                    current ^= (oppo_bit << i)
                    ptr = ptr.children[oppo_bit]
                else:
                    current ^= (bit << i)
                    ptr = ptr.children[bit]
            res = max(res, current)
        return res