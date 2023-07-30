class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        res = 0
        
        d = defaultdict(lambda: set())
        l = len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    d[i].add(j)
                    d[j].add(i)
                    
        @lru_cache(None)
        def backtrack(cur, mask):
            nonlocal res
            if mask + 1 == 1 << l:
                return 1
            ans = 0
            for i in range(l):
                if mask & (1 << i):
                    continue
                if cur in d[i]:
                    ans += backtrack(i, mask | (1 << i))
            return ans
        
        for i in range(l):
            res += backtrack(i, 1 << i)
        
        return res % (10 ** 9 + 7)