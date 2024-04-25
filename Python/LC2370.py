class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        arr = [0] * 26
        for c in s:
            i = ord(c) - 97
            l = max(0, i - k)
            r = min(25, i + k) + 1
            arr[i] = max(arr[l : r]) + 1
        return max(arr)