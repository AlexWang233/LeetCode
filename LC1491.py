class Solution:
    def average(self, salary: List[int]) -> float:
        curMin = 10 ** 6
        curMax = 1000
        total = 0
        for s in salary:
            if s > curMax:
                curMax = s
            if s < curMin:
                curMin = s
            total += s

        ans = (total - curMin - curMax) / (len(salary) - 2)
        return ans