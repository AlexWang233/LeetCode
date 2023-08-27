class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        l = len(pairs)
        pairs.sort(key = lambda x: x[1])
        ans = 0
        end = -1001
        for head, tail in pairs:
            if head > end:
                ans += 1
                end = tail
        return ans