from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        pairs = self.data[key]
        pairs.append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.data[key]
        if len(pairs) == 0 or timestamp < pairs[0][0]:
            return ""
        idx = bisect.bisect_right(pairs, [timestamp + 1])
        if idx:
            return pairs[idx - 1][1]