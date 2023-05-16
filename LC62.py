class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        m -= 1
        n -= 1

        if n > m:
            n, m = m, n
        
        ans = j = 1

        for i in range(m+1, m+n+1):
            ans *= i
            ans = ans // j
            j += 1

        return ans