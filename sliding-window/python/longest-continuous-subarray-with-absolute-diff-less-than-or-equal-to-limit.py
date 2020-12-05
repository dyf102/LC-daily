import heapq
import bisect
from collections import deque

class Solution:
    
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """LC 1438
        Time complexity: O(N)
        Space: O(N)
        Args:
            nums (List[int]): [description]
            limit (int): [description]

        Returns:
            int: [description]
        """
        n = len(nums)
        if n <= 1: 
            return 1
        min_heap = []
        max_heap = []
        longest = 0
        j = 0
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            while -max_heap[0][0] - min_heap[0][0] > limit:
                j = min(max_heap[0][1], min_heap[0][1]) + 1
                while len(min_heap) > 0 and min_heap[0][1] < j: # remove out-of-range elems
                    heapq.heappop(min_heap)
                while len(max_heap) > 0 and max_heap[0][1] < j: # remove out-of-range elems
                    heapq.heappop(max_heap)
            longest = max(longest, i - j + 1)
        return longest

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """Naive method
        Runtime: O(N^2) removing element from list takes O(N)
        """
        j = res = 0
        window = []

        for i, num in enumerate(nums):
            bisect.insort(window, num)
            if window[-1] - window[0] > limit:
                window.pop(bisect.bisect_left(window, nums[j]))
                j += 1
            res = max(res, i - j + 1)
        return res

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # deque version
        max_que = deque()
        min_que = deque()
        j = res = 0
        for i, num in enumerate(nums):
            while len(max_que) > 0 and max_que[-1][0] < num: max_que.pop()
            while len(min_que) > 0 and min_que[-1][0] > num: min_que.pop()
            max_que.append((num, i))
            min_que.append((num, i))
            if max_que[0][0] - min_que[0][0] > limit:
                if max_que[0][1] == j:
                    max_que.popleft()
                if min_que[0][1] == j:
                    min_que.popleft()
                j += 1
            res = max(res, i - j + 1)
        return res
