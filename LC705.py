class MyHashSet:

    def __init__(self):
        self.arr = [[] for _ in range(1 << 15)]

    def add(self, key: int) -> None:
        code = self.hash(key)
        if key not in self.arr[code]:
            self.arr[code].append(key)

    def remove(self, key: int) -> None:
        code = self.hash(key)
        if key in self.arr[code]:
            self.arr[code].remove(key)

    def contains(self, key: int) -> bool:
        code = self.hash(key)
        return key in self.arr[code]

    def hash(self, key: int) -> int:
        return ((key*1000003) & (1<<16) - 1)>>1
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)