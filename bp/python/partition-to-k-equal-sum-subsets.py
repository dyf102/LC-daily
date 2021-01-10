class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """LC 698. Partition to K Equal Sum Subsets
            Time Complexity: O(k^N) k is up to 16(2^4)
            Space: O(N*K)
        """
        total = sum(nums)
        if total % k != 0:
            return False
        n = len(nums)
        nums.sort(reverse=True)
        
        def isPossible(idx, buckets, target):
            if idx == n and not any([bucket != target for bucket in buckets]):
                return True
            for i in range(k):
                buckets[i] += nums[idx]
                
                if buckets[i] <= target and isPossible(idx + 1, buckets, target):
                    return True
                
                buckets[i] -= nums[idx]
                if buckets[i] == 0:
                    break
            return False
        
        return isPossible(0, [0] * k, total // k)
                