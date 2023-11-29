class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        l = next(i for i in count(1) if i * i % k == 0) * 2
        vowels = set(list('aeiou'))
        seen = [defaultdict(lambda: 0) for i in range(l)]
        seen[-1][0] = 1
        res = 0
        v = 0
        for i,c in enumerate(s):
            v += 1 if s[i] in vowels else -1
            res += seen[i % l][v]
            seen[i % l][v] += 1
        return res