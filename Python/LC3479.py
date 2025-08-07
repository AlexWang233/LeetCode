class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)

        N = 1
        while N < n:
            N *= 2
        
        seg_tree = [-1] * 2 * N
        for i in range(n):
            seg_tree[N + i] = baskets[i]

        for i in range(N - 1, 0, -1):
            seg_tree[i] = max(seg_tree[i * 2], seg_tree[i * 2 + 1])

        ans = 0
        for f in fruits:
            i = 1
            if f > seg_tree[i]:
                ans += 1
                continue

            while i < N:
                i *= 2
                if seg_tree[i] < f:
                    i += 1
            
            seg_tree[i] = -1
            while i > 1:
                i //= 2
                seg_tree[i] = max(seg_tree[2 * i], seg_tree[2 * i + 1])
            
        return ans