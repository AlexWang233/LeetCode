class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        m = val if len(self.arr) == 0 else min(val, self.arr[-1][1])
        self.arr.append([val, m])

    def pop(self) -> None:
        self.arr.pop()
        

    def top(self) -> int:
        if len(self.arr) == 0:
            return None
        return self.arr[-1][0]
        

    def getMin(self) -> int:
        if len(self.arr) == 0:
            return None
        return self.arr[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()