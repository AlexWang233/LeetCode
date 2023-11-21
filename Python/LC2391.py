class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        t = [False] * 3

        for g in garbage:
            res += len(g)

        for d in range(len(travel) - 1, -1, -1):
            for i, c in enumerate(list("MPG")):
                t[i] = t[i] or c in garbage[d + 1]
                if t[i]:
                    res += travel[d]

        return res
        