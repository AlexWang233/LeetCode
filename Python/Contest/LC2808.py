class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        l = len(nums)
        d = defaultdict(lambda:[])
        res = l // 2
        for i, n in enumerate(nums):
            d[n].append(i)
        if len(d) == 1:
            return 0
        for arr in d.values():
            if len(arr) == 1:
                continue
            cur = 0
            for i in range(len(arr) - 1):
                cur = max(cur, (arr[i + 1] - arr[i]) // 2)
            cur = max(cur, (l - arr[-1] + arr[0]) // 2)
            res = min(res, cur)

        return res
