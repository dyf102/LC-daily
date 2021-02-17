import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """LC 1675. Minimize Deviation in Array
        If the element is even, divide it by 2.
        If the element is odd, multiply it by 2.
        There are two important insights. First if the number is odd, then action 2 will convert it to even. if we
        do action 1, the number will go back, which has no change on result.
        So we can conduct multiply on all odd number, and then we divide according to descent order
        in order reduce deviation.

        """
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 1:
                nums[i] *= -2
            else:
                nums[i] *= -1
        heapq.heapify(nums)
        minimum = -max(nums)
        result = float('inf')
        while True:
            # print(nums)
            maximum = (-1) * nums[0]
            result = min(result, maximum - minimum)
            if maximum % 2 == 1:
                break
            heapq.heappushpop(nums, -(maximum // 2))
            minimum = min(minimum, maximum // 2)
        return result