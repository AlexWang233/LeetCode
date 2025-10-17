class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        arr = [0] * value
        for n in nums:
            arr[n % value] += 1
        m = min(arr)
        ans = m * value
        for i in range(value):
            if arr[i] == m:
                ans += i
                break
        return ans