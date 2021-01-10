class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """LC 1723. Find Minimum Time to Finish All Jobs
        Time complexity: O(Log(2^32)*K^N)
        Optimization: 1. sort the list reversely 
        2. stop proceeding if current bucket has nothing to put because the target is loo small 
        and there is no job larger later on.   
        """
        jobs.sort(reverse=True)
        n = len(jobs)

        def isPossible(target, buckets, idx):
            if idx == n:
                return True
            if jobs[idx] > target:
                return False
            for i in range(k):
                buckets[i] += jobs[idx]
                if buckets[i] <= target and isPossible(target, buckets, idx + 1):
                    return True
                buckets[i] -= jobs[idx]
                if buckets[i] == 0:
                    break
            return False
        left = jobs[0]
        right = sum(jobs)
        
        while left < right:
            m = (left + right) >> 1
            buckets = [0] * n
            if isPossible(m, buckets, 0):
                right = m
            else:
                left = m + 1
        return left