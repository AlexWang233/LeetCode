class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(lambda : 0)
        words.sort(key = lambda x : len(x))
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                dp[w] = max(dp[w], dp[w[:i] + w[i + 1:]] + 1)
        
        return max(dp.values())