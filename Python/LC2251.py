class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start, end = [], []
        for a, b in flowers:
            start.append(a)
            end.append(b)

        start.sort()
        end.sort()

        res = []
        for t in people:
            res.append(bisect_right(start, t) - bisect_left(end, t))

        return res
