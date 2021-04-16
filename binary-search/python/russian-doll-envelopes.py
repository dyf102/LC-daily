class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """LC 354. Russian Doll Envelopes
        Similar to longest increasing subsequence
        but O(N^2) solution will lead timeout
        the original envelops is sorted ascendly by first key
        and descendly by second key. The reason we need handle the case
        when the x are the same like [5, 4], [5, 6], they can't be
        part of result.
        time complexity: O(N*Log(N)) 
        Args:
            envelopes (List[List[int]]): [description]

        Returns:
            int: [description]
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        lls = []
        def binary_search(target):
            left = 0
            right = len(lls)

            while left < right:
                m = (left + right) // 2
                if target > lls[m][1]:
                    left = m + 1
                else:
                    right = m
            return left
        
        for envelop in envelopes:
            idx = binary_search(envelop[1])
            if idx == len(lls):
                lls.append(envelop)
            else:
                lls[idx] = envelop
        return len(lls)