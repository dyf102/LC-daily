from typing import List


def employeeFreeTime(schedule):
    """LC 759. Employee Free Time
    For the case [1,2][2,4] we shouldn't see any gap in between so when we sort the delta
    we need put start in frant of end. it basicatlly combines two slots together.
    """
    result = []
    
    delta = []
    for person in schedule:
        for event in person:
            delta.append((event[0], 0))
            delta.append((event[1], 1))
    delta.sort()
    status = 0
    prev = -1
    for t, v in delta:
        if prev != -1 and status == 0:
            result.append([prev, t])
        status += 1 if v == 0 else -1 
        prev = t
    return result
if __name__ == "__main__":
    # print(employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]))
    # print(employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]]))
    print(employeeFreeTime([[[7,24],[29,33],[45,57],[66,69],[94,99]],[[6,24],[43,49],[56,59],[61,75],[80,81]],[[5,16],[18,26],[33,36],[39,57],[65,74]],[[9,16],[27,35],[40,55],[68,71],[78,81]],[[0,25],[29,31],[40,47],[57,87],[91,94]]]))