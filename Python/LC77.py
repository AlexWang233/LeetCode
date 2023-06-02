class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def cb(comb: List[int], start: int):
            if len(comb) == k:
                ans.append(comb.copy())
            else:
                for i in range(start, n+2-k+len(comb)):
                    cb(comb + [i], i+1)
        
        cb([], 1)
        return ans

