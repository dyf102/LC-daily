from collections import defaultdict
import bisect

class MyCalendarThree:
    def __init__(self):
        self.delta = []
        self.value = defaultdict(int)
    def book(self, start: int, end: int) -> int:
        """
        keep a ordered map to store the delta
        each start add one, each end add minus one

        Args:
            start (int): [description]
            end (int): [description]

        Returns:
            int: max of number of overbook
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
        res = 0
        count = 0
        for i, v in enumerate(self.delta):
            count += self.value[v]
            res = max(count, res)
        return res



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)