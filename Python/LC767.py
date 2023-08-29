class Solution:
    def reorganizeString(self, s: str) -> str:
        l = len(s)
        counter = Counter(s)
        arr = sorted(counter.keys(), key = lambda c: counter[c], reverse=True)
        if counter[arr[0]] > (l + 1) // 2:
            return ""
        res = ['']*l
        i = 0
        for c in arr:
            for _ in range(counter[c]):
                if i >= l:
                    i = 1
                res[i] = c
                i += 2

        return ''.join(res)
