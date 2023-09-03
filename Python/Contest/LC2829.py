class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        mid = k // 2
        if n <= mid:
            return n * (n + 1) // 2
        l_sum = mid * (mid + 1) // 2
        r = n - mid
        r_sum = r * (2 * k + r - 1) // 2
        return l_sum + r_sum