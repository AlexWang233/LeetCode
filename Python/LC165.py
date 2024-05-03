class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        for i, j in zip_longest(v1, v2, fillvalue=0):
            if i == j:
                continue
            return -1 if i < j else 1
        return 0