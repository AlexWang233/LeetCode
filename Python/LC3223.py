class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        for c in string.ascii_lowercase:
            if counter[c] == 0:
                continue
            if counter[c] % 2 == 0:
                ans += 2
            else:
                ans += 1
        return ans