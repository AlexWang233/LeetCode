class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        if l3 == 0:
            return True
        i = 0
        cur = set([(-1, -1)])
        while cur:
            nxt = set()
            for j, k in cur:
                if j + 1 < l1 and s1[j + 1] == s3[i]:
                    nxt.add((j + 1, k))
                if k + 1 < l2 and s2[k + 1] == s3[i]:
                    nxt.add((j, k + 1))
            i += 1
            cur = nxt
        return i > l3