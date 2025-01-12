class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        counter = Counter(s)
        oddCount = 0
        for val in counter.values():
            if (val % 2 == 1):
                oddCount += 1
        return oddCount <= k