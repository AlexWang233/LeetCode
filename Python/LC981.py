class TimeMap:

    def __init__(self):
        self.dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        l = len(arr)

        left, right = 0, l
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        return "" if right == 0 else arr[right - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)