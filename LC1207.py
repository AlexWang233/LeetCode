class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        for item in Counter(arr).values():
            if item in seen:
                return False
            seen.add(item)

        return True