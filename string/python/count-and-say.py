class Solution:
    @lru_cache()
    def countAndSay(self, n: int) -> str:
        """LC 38. Count and Say

        Args:
            n (int): [description]

        Returns:
            str: [description]
        """
        if n == 1:
            return "1"
        prev = int(self.countAndSay(n - 1))
        
        v = prev % 10
        count = 1
        prev //= 10
        result = []
        while prev > 0:
            ## print(prev, v)
            if prev % 10 == v:
                count += 1
            else:
                result.append("{}{}".format(count, v))
                v = prev % 10
                count = 1
            prev //= 10   
        result.append("{}{}".format(count, v))
        return "".join(result[::-1])
            