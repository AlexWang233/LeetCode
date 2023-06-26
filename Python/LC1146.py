class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[-1, 0]] for _ in range(length)]
        self.count = 0

    def set(self, index: int, val: int) -> None:
        if self.arr[index][-1][0] == self.count:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.count, val])

    def snap(self) -> int:
        self.count += 1
        return self.count - 1
        

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.arr[index], [snap_id + 1, 0]) - 1
        return self.arr[index][i][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)