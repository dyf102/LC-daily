from collections import defaultdict
import bisect

class MyCalendarTwo:

    def __init__(self):
        # maintain a ordered map
        self.delta = []
        self.value = defaultdict(int)
    def book(self, start: int, end: int) -> bool:
        """LC 731
        time complexity: O(NLog(N))
        space: O(N)
        """
        if start in self.value:
            self.value[start] += 1
        else:
            bisect.insort(self.delta, start)
            self.value[start] += 1
        
        if end in self.delta:
            self.value[end] -= 1
        else:
            bisect.insort(self.delta, end)
            self.value[end] = -1
        count = 0
        remove_idx = []
        # iterate from begining to end, sum up the delta, 
        # if the sum is greater than 2, return false
        for i, v in enumerate(self.delta):
            count += self.value[v]
            if count > 2:
                self.value[start] -= 1
                if self.value[start] == 0:
                    idx = bisect.bisect_left(self.delta, start)
                    remove_idx.append(idx)
                    del self.value[start]
                self.value[end] += 1
                if self.value[end] == 0:
                    idx = bisect.bisect_left(self.delta, end)
                    remove_idx.append(idx)
                    del self.value[end]
                self.delta = [i for j, i in enumerate(self.delta) if j not in remove_idx]
                # print(self.value, self.delta, count)
                return False
        
        return True
