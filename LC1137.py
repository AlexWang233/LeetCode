class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        if n < 3:
            return arr[n]
        for i in range(n-2):
            m = sum(arr)
            arr[0] = arr[1]
            arr[1] = arr[2]
            arr[2] = m
        return arr[2]