class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        l = len(cookies)
        distribution = [0] * k

        ans = 10 ** 7
        def backtrack(i):
            nonlocal ans
            if i == l:
                ans = min(ans, max(distribution))
                return

            if ans <= max(distribution):
                return

            for j in range(k):
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]
                
        backtrack(0)
        return ans
