class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = [count.pop(c, 0) * c for c in order]
        print(res)
        for key, val in count.items():
            res.append(key * val)
        return ''.join(res)