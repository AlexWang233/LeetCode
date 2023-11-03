class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        prev = 0
        res = []
        for n in target:
            res += ["Push" for _ in range(n - 1 - prev)]
            res += ["Pop" for _ in range(n - 1 - prev)]
            res.append("Push")
            prev = n

        return res
