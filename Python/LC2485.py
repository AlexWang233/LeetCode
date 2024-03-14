class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        i = cur = 1
        while cur < total - cur + i:
            i += 1
            cur = i * (i + 1) // 2
        if cur == total - cur + i:
            return i
        return -1