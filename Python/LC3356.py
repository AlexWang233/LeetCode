class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        n, q = len(nums), len(queries)
        freq = [0] * (n + 1)
        cur_freq = res = 0

        for i in range(n):
            while cur_freq < nums[i] - freq[i]:
                if res >= q:
                    return -1
                l, r, val = queries[res]
                if r >= i:
                    freq[max(l, i)] += val
                    freq[r + 1] -= val
                res += 1
            cur_freq += freq[i]
        
        return res
