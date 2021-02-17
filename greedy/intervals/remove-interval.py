from typing import List
import bisect


def removeInterval(intervals: List[List[int]], toBeRemoved: List) -> List[List[int]]:
    """[summary]
    Example 1:

    Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
    Output: [[0,1],[6,7]]
    Example 2:

    Input: intervals = [[0,5]], toBeRemoved = [2,3]
    Output: [[0,2],[3,5]]
    Args:
        intervals (List[List[int]]): [description]
        toBeRemoved (List): [description]

    Returns:
        List[List[int]]: [description]
    """
    n = len(intervals)
    starts, ends = zip(*[(interval[0], interval[1]) for interval in intervals])
    idx = bisect.bisect_left(starts, toBeRemoved[0])
    if idx == len(intervals):
        if toBeRemoved[0] < ends[-1]:
            intervals[-1][1] = toBeRemoved[0]
            if toBeRemoved[1] < ends[-1]:
                intervals.append([toBeRemoved[1], ends[-1]])
        return intervals
    result = []
    for i in range(idx):
        if ends[i] <= toBeRemoved[0]:
            result.append(intervals[i])
        else:
            result.append([starts[i], toBeRemoved[0]])
    
    for i in range(idx, n):
        if starts[i] >= toBeRemoved[1]:
            result.append(intervals[i])
        elif ends[i] > toBeRemoved[1]:
            result.append([toBeRemoved[1], ends[i]])
    return result

if __name__ == "__main__":
    print(removeInterval([[0,2],[3,4],[5,7]], [1,6]))
    # assert  == [[0,1],[6,7]]
    print(removeInterval([[0,5]], [2,3]))
    # assert removeInterval([[0,5]], [2,3]) == [[0,2],[3,5]]