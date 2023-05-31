class UndergroundSystem:

    def __init__(self):
        self.customers = defaultdict(lambda: ("", -1))
        self.avgTime = defaultdict(lambda: (0, 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (start, prevT) = self.customers[id]
        (total, count) = self.avgTime[(start, stationName)]
        self.avgTime[(start, stationName)] = (total + t - prevT, count + 1)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        (total, count) = self.avgTime[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)