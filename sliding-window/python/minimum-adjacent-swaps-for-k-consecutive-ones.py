
def minMoves(self, nums: List[int], k: int) -> int:
    """LC 1703 Minimum Adjacent Swaps for K Consecutive Ones
    Difficulty: Hard
    Time complexity: O(N)
    Space: O(N)

    Args:
        nums (List[int]): [description]
        k (int): [description]

    Returns:
        int: [description]
    """
    idxs = [i for i, v in enumerate(nums) if v == 1]
    m = len(idxs)
    partial_sum = [0] * (m + 1)
    for i in range(m):
        partial_sum[i + 1] = partial_sum[i] +idxs[i]
    res = float('inf')
    if k % 2 == 1:
        radius = (k - 1) // 2
        for i in range(radius, m - radius):
            left = partial_sum[i] - partial_sum[i - radius]
            right = partial_sum[i + radius + 1] - partial_sum[i + 1]
            res = min(res, right - left)
        return res - (radius) * (radius + 1)
    else:
        radius = (k - 2) // 2
        for i in range(radius, m - radius - 1):
            right = partial_sum[i + radius + 2] - partial_sum[i + 1]
            # i-radius...i-1
            left = partial_sum[i] - partial_sum[i - radius]
            res = min(res, right - left - idxs[i])
        return res - radius * (radius + 1) - (radius + 1)
    