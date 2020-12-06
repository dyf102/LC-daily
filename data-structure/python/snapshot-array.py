import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.data = [[[0, 0]] for _ in range(length)]
        self.version_num = 0
        self.length = length
    def set(self, index: int, val: int) -> None:
        if index > self.length - 1:
            return
        versions = self.data[index]
        versions.append([self.version_num, val])

    def snap(self) -> int:
        self.version_num += 1
        return self.version_num - 1

    def get(self, index: int, snap_id: int) -> int:
        if index > self.length - 1:
            return
        idx = bisect.bisect_left(self.data[index], [snap_id + 1]) - 1
        return self.data[index][idx][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)