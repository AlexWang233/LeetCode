class SmallestInfiniteSet:

    def __init__(self):
        self.curMin = 0
        self.backList = []

    def popSmallest(self) -> int:
        if len(self.backList) == 0:
            self.curMin += 1
            return self.curMin
        else:
            return heapq.heappop(self.backList)

    def addBack(self, num: int) -> None:
        if num - 1 < self.curMin and num not in self.backList:
            heapq.heappush(self.backList, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)