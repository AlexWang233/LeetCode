class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        res = 0
        for key, value in c.items():
            res += ceil(value / (key + 1)) * (key + 1)

        return res