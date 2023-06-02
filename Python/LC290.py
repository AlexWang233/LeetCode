class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        l = len(arr)
        if l != len(pattern):
            return False
        d = defaultdict(lambda:'')
        for i, p in enumerate(pattern):
            if p in d:
                if d[p] != arr[i]:
                    return False
            else:
                if arr[i] in d.values():
                    return False
                d[p] = arr[i]

        return True