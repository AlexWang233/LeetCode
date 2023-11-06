class SeatManager:

    def __init__(self, n: int):
        self.hp = list(range(1, n + 1))

    def reserve(self) -> int:
        return heapq.heappop(self.hp)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.hp, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)