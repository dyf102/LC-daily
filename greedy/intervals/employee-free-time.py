from typing import List

def employeeFreeTime(schedule : List[List[int]]):
    deltas = []
    result = []
    for individual in schedule:
        for shift in individual:
            deltas.append((shift[0], 1))
            deltas.append((shift[1], -1))
    
    deltas.sort()

    current = 0
    start = -1
    for time, v in deltas:
        current += v
        if current == 0:
            start = time
        elif start != -1:
            result.append([start, time])
            start = -1
    return result

if __name__ == "__main__":
    print(employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]))
    print(employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]]))