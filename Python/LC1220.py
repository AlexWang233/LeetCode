class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        mod = 10**9 + 7
        a = e = i = o = u = 1
        
        for _ in range(1, n):
            a2 = e
            e2 = (a + i) % mod
            i2 = (a + e + o + u) % mod
            o2 = (i + u) % mod
            u2 = a
            a, e, i, o, u = a2, e2, i2, o2, u2
        
        return (a + e + i + o + u) % mod