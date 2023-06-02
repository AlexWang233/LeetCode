class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        i = bisect.bisect_left(self.arr, num)
        self.arr.insert(i, num)

    def findMedian(self) -> float:
        l = len(self.arr)
        if l % 2:
            return self.arr[l // 2]
        return (self.arr[l // 2 - 1] + self.arr[l // 2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()