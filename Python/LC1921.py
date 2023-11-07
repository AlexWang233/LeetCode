class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        l = len(dist)
        arr = []
        for i in range(l):
            arr.append(1 + (dist[i] - 1) // speed[i])

        arr.sort()

        for i, n in enumerate(arr):
            if n <= i:
                return i

        return l

        