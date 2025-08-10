class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1:
            return True
        c = Counter(str(n))
        l = len(str(n))
        m = 1
        c2 = Counter(str(m))
        while sum(c2.values()) <= l:
            m *= 2
            c2 = Counter(str(m))
            if c2 == c:
                return True
        return False
