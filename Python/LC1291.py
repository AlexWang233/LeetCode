class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        for i in range(1, 10):
            n = i
            d = i + 1
            while n <= high and d <= 9:
                n *= 10
                n += d
                if low <= n <= high:
                    res.append(n)
                d += 1
        
        res.sort()
        return res
