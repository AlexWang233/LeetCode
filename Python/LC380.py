class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = dict()

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            last = self.arr[-1]
            ind = self.map[val]
            self.map[last] = ind
            self.arr[ind] = last
            self.arr.pop()
            self.map.pop(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()