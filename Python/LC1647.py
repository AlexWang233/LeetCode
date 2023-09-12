class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        visited = set()
        res = 0
        for c, freq in count.items():
            while freq > 0 and freq in visited:
                freq -= 1
                res += 1
            visited.add(freq)
        return res