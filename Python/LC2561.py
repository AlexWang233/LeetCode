class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        min_val = min(min(basket1), min(basket2))
        s = set()
        c = Counter(basket1)
        for b in basket2:
            c[b] = c.get(b, 0) - 1

        for val in c.values():
            if val % 2 == 1:
                return -1

        arr = []
        for key, val in c.items():
            for _ in range(abs(val) // 2):
                arr.append(key)

        arr.sort()
        res = 0
        for i in arr[:len(arr) // 2]:
            res += min(i, 2 * min_val)

        return res