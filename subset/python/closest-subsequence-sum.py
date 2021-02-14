import bisect

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        """LC 1755. Closest Subsequence Sum
        1. Use dp to generate subset sum candidates(2^(N/2))
        2. sorted the two parts' subset sums (2 * 2^(N/2)* N / 2) = N * 2^(N / 2)
        3. binary search to find closest set
            - Candidate 1: left_subsets[idx]
            - Candidate 2: left_subsets[idx - 1]
        Optimization: 
        1. avoid sort on big combination sums, we can merge sorted lists step by step
        2. use two pointer approach to find closest sum in two sorted list( NLog(N) => O (N))
        """
        n = len(nums)
        left_subsets = [0]
        right_subsets = [0]
        for i in range(n // 2):
            m = len(left_subsets)
            for j in range(m):
                left_subsets.append(left_subsets[j] + nums[i])
        
        for i in range(n // 2, n):
            m = len(right_subsets)
            for j in range(m):
                right_subsets.append(right_subsets[j] + nums[i])
        left_subsets.sort()
        right_subsets.sort()
        result = float('inf')
        for num in right_subsets:
            idx = bisect.bisect_left(left_subsets, goal - num)
            if idx != len(left_subsets):
                result = min(result, abs(goal - num - left_subsets[idx]))
            if idx != 0:
                result = min(result, abs(goal - num - left_subsets[idx - 1]))
        for num in left_subsets:
            idx = bisect.bisect_left(right_subsets, goal - num)
            if idx != len(right_subsets):
                result = min(result, abs(goal - num - right_subsets[idx]))
            if idx != 0:
                result = min(result, abs(goal - num - right_subsets[idx - 1]))
        return result

        def minAbsDifference(self, nums: List[int], goal: int) -> int:
            n = len(nums)
            left_subsets = [0]
            right_subsets = [0]
            
            for i in range(n // 2):
                m = len(left_subsets)
                for j in range(m):
                    left_subsets.append(left_subsets[j] + nums[i])
            
            for i in range(n // 2, n):
                m = len(right_subsets)
                for j in range(m):
                    right_subsets.append(right_subsets[j] + nums[i])
            left_subsets.sort()
            right_subsets.sort()
            result = float('inf')
            j = len(right_subsets) - 1
            for i in range(len(left_subsets)):
                while j >= 0 and right_subsets[j] + left_subsets[i] > goal:
                    result = min(result, abs(goal - (right_subsets[j] + left_subsets[i])))
                    j -= 1
                if j >= 0:
                    result = min(result, abs(goal - (right_subsets[j] + left_subsets[i])))
                
            return result