class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        mod = 10 ** 9 + 7
        l = len(target)
        ans = [1] + [0] * l

        for i in range(len(words[0])):
            cur = collections.Counter(w[i] for w in words)
            for j in range(l - 1, -1, -1):
                ans[j + 1] += ans[j] * cur[target[j]]
                ans[j + 1] %= mod

        return ans[-1] % mod
