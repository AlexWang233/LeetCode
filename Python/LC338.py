class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        arr = [0, 1]
        while len(arr) <= n:
            cur = []
            for i in range(min(len(arr), n - len(arr)+1)):
                cur.append(1 + arr[i])
            arr += cur
        return arr