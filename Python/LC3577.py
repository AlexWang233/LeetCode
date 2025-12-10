class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        m = 10 ** 9 +7
        min_complexity = complexity[0]
        for i in complexity[1:]:
            if i <= min_complexity:
                return 0
        ans = 1
        for i in range(2, len(complexity)):
            ans *= i
            ans %= m
        return ans