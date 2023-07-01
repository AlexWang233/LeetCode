class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        l = len(cookies)
        distribution = [0] * k

        # algorithm to produce preliminary result
        hq = [0] * k
        cookies.sort(reverse = True)
        for c in cookies:
            # see which child has least cookies and give them current bag
            n = heapq.heappop(hq)  
            n += c
            heapq.heappush(hq, n)
        ans = max(hq)


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
        
        # backtrack afterwards since prelim result is better than initial worst case (all cookies to 1 person)
        backtrack(0)
        return ans
