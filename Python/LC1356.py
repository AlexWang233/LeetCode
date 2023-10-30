class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda a: [bin(a).count('1'), a])
        return arr