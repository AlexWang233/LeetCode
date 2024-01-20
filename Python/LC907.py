class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr + [0]
        l = len(arr)
        stk = []
        res = 0
        mod = 10 ** 9 + 7

        for i in range(l):
            while stk and arr[stk[-1]] > arr[i]:
                mid = stk.pop()
                left = stk[-1]
                right = i
                res += arr[mid] * (mid - left) * (right - mid)
            stk.append(i)
        return res % mod
        