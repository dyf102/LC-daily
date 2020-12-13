import bisect

class MyCalendar:

    def __init__(self):
        self.delta = []

    def book(self, start: int, end: int) -> bool:
        idx1 = bisect.bisect_left(self.delta, (start, 1))
        self.delta.insert(idx1, (start, 1))
        idx2 = bisect.bisect_left(self.delta, (end, -1))
        self.delta.insert(idx2, (end, -1))
        count = 0
        for i, j in self.delta:
            count += j
            if count > 1:
                del self.delta[idx2]
                del self.delta[idx1]
                return False
        return True
    
    def book(self, start: int, end: int) -> bool:
        # find the insert point, because the end is in open interval, so we need use bisect right
        idx1 = bisect.bisect_right(self.delta, start) 
        if idx1 % 2 == 1: # if there is odd number in front of start, the start is within one interval
            return False
        
        idx2 = bisect.bisect_left(self.delta, end)
        if idx1 != idx2: # if there is no interval falling in between, we can get two idxs the same
            return False
        self.delta = self.delta[:idx1] + [start, end] + self.delta[idx1:]
        return True
                
                