class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        l = len(ranges) - 1
        arr = []
        for i, r in enumerate(ranges):
            if r == 0:
                continue
            else:
                arr.append((max(0, i - r), min(l, i + r)))
        arr = sorted(arr, key = lambda x: (x[0], -x[1]))
        cur = 0
        cur_end = 0
        res = 0
        for start, end in arr:
            if start > cur:
                cur = cur_end
                res += 1
            if cur == l:
                return res
            if start > cur:
                return -1
            else:
                cur_end = max(cur_end, end)
        if cur_end == l:
            return res + 1
        else:
            return -1
