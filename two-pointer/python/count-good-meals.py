from collections import Counter
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        """LC 1711 Count Good Meals
        Time Complexity: O(22N)
        Space: O(N)
        Difficuty: Medium
        """
        res = 0
        counter = Counter()
        mod = 10**9 + 7
        for num in deliciousness:
            for i in range(22):
                c =  counter.get((1 << i) - num)
                if c is not None:   
                    res += c
                    res %= mod
            counter[num] += 1
        return res