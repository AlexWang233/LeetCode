class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l = len(arr)
        l2 = l // 4
        for i in range(l - l2):
            if arr[i] == arr[i + l2]:
                return arr[i]

        return -1