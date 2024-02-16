class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        c = list(counter.values())
        c.sort()
        l = len(c)
        cur = 0
        for i in range(l):
            cur += c[i]
            if cur > k:
                return l - i
        return 0