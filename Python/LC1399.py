class Solution:

    def digitSum(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n % 10
            n //= 10
        return res

    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(lambda: 0)

        for i in range(1, n + 1):
            j = self.digitSum(i)
            d[j] += 1

        curMax = 0
        res = 0
        
        for val in d.values():
            if val > curMax:
                curMax = val
                res = 0
            if val == curMax:
                res += 1
        return res

        