class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packetSet = set()
        self.packetQueue = deque()
        self.packetCount = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = tuple([source, destination, timestamp])
        if packet in self.packetSet:
            return False
        while len(self.packetQueue) >= self.memoryLimit:
            self.forwardPacket()
        self.packetQueue.append(packet)
        self.packetSet.add(packet)
        self.packetCount[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.packetQueue) == 0:
            return []
        packet = self.packetQueue.popleft()
        self.packetSet.remove(packet)
        self.packetCount[packet[1]].pop(0)
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.packetCount[destination]
        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)