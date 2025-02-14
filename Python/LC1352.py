class ProductOfNumbers:
    def __init__(self):
        self.arr = []
        self.prod = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = []
            self.prod = 1
        else:
            self.prod *= num
            self.arr.append(self.prod)

    def getProduct(self, k: int) -> int:
        if len(self.arr) < k:
            return 0
        if len(self.arr) == k:
            return self.arr[-1]
        return self.arr[-1] // self.arr[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)