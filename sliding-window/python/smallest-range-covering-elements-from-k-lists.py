class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        if n == 0: return 0
        idxs = [0] * n
        
        window = [(nums[i][idx], i) for i, idx in enumerate(idxs)]
        heapq.heapify(window)
        upper = max(window, key=itemgetter(0))[0]
        lower = window[0][0]
        result_lower, result_upper = lower, upper
        while len(window) == n:
            smallest, idx = heapq.heappop(window)
            
            if idxs[idx] + 1 < len(nums[idx]):
                idxs[idx] += 1
                next_val = nums[idx][idxs[idx]]
                heapq.heappush(window, (next_val, idx))
                lower = window[0][0]
                upper = max(upper, next_val) 
                
                if upper - lower < result_upper - result_lower:
                    result_upper = upper
                    result_lower = lower
        return [result_lower, result_upper]
